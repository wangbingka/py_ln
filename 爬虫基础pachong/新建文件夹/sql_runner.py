# -*- coding: UTF-8 -*-
'''
 * Created by yangfan on 2018/03/08.
'''
import requests
import time
import os
import uuid
import threading

ENCODING = 'utf-8'
USER = "medicalquality"  #"fan.yang"
TOKEN = "48c0780fda80bb51e1350ac1aa6083a7" #"3caa315fcff93e6137f5c37eb920e204"
result = {}
_result = {}
PWD = "Fany.810818"
AZ_HOST = "http://azkaban.intra.yiducloud.cn/azkaban-proxy"
INTERVAL = 60
INVALID_STATUS = ['FAILED', "Skip", "KILLED"]
END_STATUS = ["KILLED", 'FAILED', "SUCCEEDED"]

ClusterJobPending = {}

nginx_proxy_session = "ZyEZrzVFWW-v1XFzuCH3vg..|1930844679|emUxL-bmQjPsMT1YdC653TLHKgI." # 每日更新

session = requests.session()
requests.utils.add_dict_to_cookiejar(session.cookies,{"nginx_proxy_session":nginx_proxy_session})

def get_target_database(cluster, type='etldr', product='nova'):
    database = "" if not cleanflag else "clean"
    hulk_url = 'http://hulk.m.com/api/hulk/database/getlatest'
    parames = {"type": type,
                "hospital_code": cluster,
                 "product":product}
    rsp = session.get(url=hulk_url, params=parames, timeout=200)
    if rsp.status_code == 200:
        data = rsp.json()['data']

        if 'database' in data:
            database = "%s%s"% (data['database'], database)
            # print cluster,"-database:", database
            result[cluster] = {'database': database}
    parames["product"] = u'专病'
    rsp = requests.get(url=hulk_url, params=parames, timeout=30)
    if rsp.status_code == 200:
        data = rsp.json()['data']

        if 'database' in data:
            database = "%s%s"% (data['database'], database)
            # print cluster,"-database:", database
            result[cluster] = {'database': database}
        elif 'all' in data:
            d_all = data['all']
            for d in d_all:
                release = d['release']
                if release == 1:
                    database = "%s%s"% (d['database'], database)
                    result[cluster] = {'database': database}
                    break
        else:
            _result[cluster] = {'database': database}
            print cluster, '[WARN] get %s : No target database found' % rsp.url

        return database


def get_database_from_file(filepath, t_cluster):
    print "Get db from %s ..." % filepath
    if t_cluster:
        print "filter cluster in %s:" % t_cluster
    clean = "" if not cleanflag else "clean"
    t_cluster_list = []
    if t_cluster:
        t_cluster_list = t_cluster.strip().split(",")
    n = 0
    # print t_cluster_list, repr(t_cluster)
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            # print "line",line
            linedata = line.split()
            if not linedata or line.startswith('#'):
                continue
            cluster = linedata[0]
            dbname = linedata[1]
            if t_cluster_list and not cluster in t_cluster_list:
                continue
            if "schema" in dbname:
                clean = ""
            result[cluster] = {'database': "%s%s" % (dbname, clean)}
            n += 1
            # print n, cluster, result[cluster]['database']


def request_az(rdata):
    az_url = AZ_HOST + '/schedule'
    result = None
    try:
        response = session.post(url=az_url, data=rdata, timeout=100)
        if response.status_code == 200:
            result = response.json()
        else:
            msg = "[Error]Post %s [%d], response:" % (az_url, response.status_code), response.text
            print msg
    except Exception,e:
        print '[Exception]',e,"response:",response.text
    finally:
        return result


def get_cluster(cluster):
    if cluster.startswith('bjcancer'):
        return 'bjcancer'
    elif cluster.endswith('cqmu') and cluster != "cqmu":
        return 'uhcmu'
    else:
        return cluster
    return


def get_hive_excutor_job(cluster, sqlfile):
    print "cluster:",cluster,
    database = result[cluster].get('database')
    print "database:", database
    if database == '':
        print cluster, "no database."
        exit(-1)
    job = {
        "cluster": cluster,
        "database": database,
        "status": "None",
        "project": "None",
        "execid": "None"
    }
    with open(sqlfile) as f:

        sql = f.read()
        import chardet
        print sqlfile, chardet.detect(sql)
        sql2 = "set mapred.job.name=%s_%s;\n" % (appname, str(uuid.uuid1()))+sql.decode('utf-8').replace('%s', database).replace('\"', '\'')
        print "sql2",type(sql2)

    print "sql2:", sql2.encode(ENCODING)
    #cdata = "cluster=qyfy&method=run&user=fan.yang&token=7f722bbb7fab53b82c14bb9141f96192&jobType=sql_executor&jobParams={\"input\":\"-n default -s testsql -t local -f /user/data/etldr/test \"}&jobFiles={\"file\":'select * from qyfy_20171026_200_2_etldr.tbl_adt_admits_discharges a limit 1;'}"
    rdata = {
        "cluster": cluster,
        "method": "run",
        "user": USER,
        "token": TOKEN,
        "jobType": "hive",
        "jobParams": "{\"hiveSql\":\"%s\"}" % sql2,
    }
    print "executor request data:", rdata
    resp = request_az(rdata)
    project = ""
    execid = ""
    print "resp",resp
    if resp:
        project = resp.get('project')
        execid = resp.get('execid')
    if project and execid:
        append_pending_jobs(cluster, project, execid)
        job["project"] = project
        job['execid'] = execid
        time.sleep(5)
        status = get_exec_status(cluster, project, execid)
        job['status'] = status
        print "cluster:", cluster, " project:", project, " execid:", execid, "status:", status
    return job


def get_exec_status(cluster, project, execid):
    if not project or not execid:
        return "Skip next step, due to no project or execid."
    status = "No-reget"
    sdata = {
        "cluster": cluster,
        "project": project,
        "method": "fetchjobStatus",
        "user": USER,
        "token": TOKEN,
        "execid": execid
    }
    resp = request_az(sdata)
    if resp:
        status = resp.get('status')
    return status


def wait_pending_jobs(cluster, max=5, interval=2):
    global ClusterJobPending
    if not ClusterJobPending.get(cluster): # 没有等待队列
        return
    time.sleep(interval)
    n = 0
    while len(ClusterJobPending[cluster]) >= max:
        time.sleep(60*interval)  # 队列间隔interval分钟后更新
        running_joblist = []
        joblist = ClusterJobPending[cluster]
        print "==== %s wait_pending_jobs | max: %d ====" % (cluster, max)
        for job in joblist:
            project, execid = job[:2]
            status = get_exec_status(cluster, project, execid)
            if status not in END_STATUS:
                print "    * %s %s %s ..." % ( project, execid, status)
                running_joblist.append([project, execid])
        ClusterJobPending[cluster] = running_joblist
        n += 1
        if n >= 2 and max >= 2: # 等待时间越长，减少并行数
            max = max - 1

    if n > 0:
        print "\n waiting for az-schedule running on %s for %d minutes." % (cluster, n*5)


def append_pending_jobs(cluster, project, execid):
    global ClusterJobPending
    if cluster not in ClusterJobPending:
        ClusterJobPending[cluster] = []  #初始化

    ClusterJobPending[cluster].append([project, execid])


def get_query_data(cluster, project):

    qdata = {
        "cluster": cluster,
        "method": "fetchJobResult",
        "user": USER,
        "token": TOKEN,
        "project": project
    }
    resp = request_az(qdata)
    if resp:
        return resp


def convert_unicode(unicodeo):
    """
    将字符串的unicode编码转为utf8编码的str
    :param unicodeo: 
    :return: 
    """
    if not isinstance(unicodeo, unicode):
        unicodeo = unicode(unicodeo)
        value = str(unicodeo).replace('u\'', '\'').decode("unicode-escape")
    else:
        value = unicodeo
    return value.encode(ENCODING)



def runone(cluster, delay=10):
    time.sleep(delay)
    global sqlfiles

    print "\n-------- start on %s --------\n" % cluster
    for sql in sqlfiles:
        wait_pending_jobs(cluster=cluster, max=1, interval=1) # max为最大并行数 interval是队列更新的更新时间
        job = get_hive_excutor_job(cluster, os.path.join("./sql",sql))
        generate_rest(job, sql)
    print "\n-------- end on %s --------\n" % cluster
    if not sqlfiles:
        exit(0)
    print"\n Wait for 5 minutes to get rest data ..."
    time.sleep(5*60)
    get_all_rest() # 等五分钟后自动取结果


def runall():
    # global result
    cluster_list = result.keys()
    for n, cluster in enumerate(cluster_list):
        database = result[cluster].get('database')
        print n+1, cluster, database

    tsk = []
    for n,cluster in enumerate(cluster_list):
        try:
            thread = threading.Thread(target=runone,args=(cluster, 2*n))
            tsk.append(thread)
        except:
            print "Error: unable to start thread %d-%s" % (n, cluster)
    for t in tsk:
        t.start()

    for t in tsk:
        threading.Thread.join(t)
    print "End run all"
    # show_rest()


def generate_result(cluster, sql):
    if cluster not in result:
        return

    data = result[cluster].get('data',"")
    status = result[cluster]['status']
    if status == 'SUCCEEDED':
        filename = "result/%s_%s_%s.txt" % (sql, cluster, result[cluster]['database'])
        with open(filename, 'w') as f:
            f.write(data.encode(ENCODING))


def generate_rest(job, sql):
    row = "%(cluster)s\t%(database)s\t%(status)s\t%(project)s\t%(execid)s\n" % job
    if not row.endswith("\n"):
        row = "%s\n" % row
    restfile = 'rest/%s_rest.txt' % sql
    with open(restfile, 'a') as f:
        f.write(row.encode(ENCODING))
        print "%s saved." % restfile


def get_rest_data(sql):
    filepath = 'rest/%s_rest.txt' % sql
    if not os.path.exists(filepath):
        print "%s not exitsts.SKIP" % filepath
        return

    update_rest = ""
    with open(filepath, 'r') as f:
        for line in f.readlines():
            endflag = False
            linedata = line.strip().split()
            if not linedata or line.startswith('#') or line.startswith('-'):
                update_rest += line
                continue
            cluster = linedata[0]
            database = linedata[1]
            status = linedata[2]
            project = linedata[3]
            execid = linedata[4]
            result[cluster] = {'database': database,
                               'status':status,
                               'project': project,
                               'execid': execid}
            print "cluster:database:project:execid:old-status", cluster, database, project, execid, status
            # print status in INVALID_STATUS and project != "None"
            if status not in INVALID_STATUS and project != "None":
                # 再次取查询数据
                status = get_exec_status(cluster, project, execid)
                print cluster, "exec status:", status
                if status == 'SUCCEEDED':
                    result[cluster]['status'] = status
                    r = get_query_data(cluster, project)
                    print cluster, "SQL Result:", r, "Convert format:", convert_unicode(r)
                    if 'warn' in r:
                        print r['warn'].encode(ENCODING)
                    elif 'error' in r:
                        print r['error'].encode(ENCODING)
                    elif 'data' in r:
                        data = r['data']
                        result[cluster]['data'] = data
                        generate_result(cluster,sql)
                        endflag = True

            if not endflag:
                nline = "%s\t%s\t%s\t%s\t%s\n" % (cluster, database, status, project, execid)
            else:
                nline = "#%s\t%s\t%s\t%s\t%s\n" % (cluster, database, status, project, execid)
            update_rest += "%s" % nline

    os.rename(filepath, "%s.bak" % filepath)
    with open(filepath, 'w') as fw:
        print "update rest txt :%s" % filepath
        fw.write(update_rest.encode(ENCODING))


def get_all_rest():
    print "Get all rest data..."
    global sqlfiles
    resttsk = []
    for sql in sqlfiles:
        try:
            restfile = 'rest/%s_rest.txt' % sql
            # print "restfile:",restfile,len(restfile)
            restthread = threading.Thread(target=get_rest_data, args=(sql,))
            resttsk.append(restthread)
        except:
            print "Error: unable to start thread -%s" % (sql)
    for t in resttsk:
        t.start()

    for t in resttsk:
        threading.Thread.join(t)
    print "End get all rest."


def get_cluster_dict():
    global clusterdict
    clusterdict = {}
    try:
        url = "http://openapi.intra.yiducloud.cn/openapi/cluster/list"
        r = requests.get(url=url, timeout=30)

        for x in r.json()['value'].values():
            clusterdict[x['id']] = x['name']
    except Exception,e:
        msg = "[exception]Get %s:%s" % (url, str(e))
        print msg


def filter_sql_file(path="./sql", s_sqlid='R001,R002'):
    sql_files = []
    s_sqlid = s_sqlid.replace(" ", "")

    for file in os.listdir(path):
        if file.endswith('.sql'):
            if (cleanflag and not 'before' in file) or (not cleanflag and 'before' in file):
                sql_files.append(file)

    if s_sqlid.lower() == 'all':
        return sql_files
    r_result = []
    s_sqlids = s_sqlid.split(',')
    for sqlid in s_sqlids:
        idsql = "%s.sql" % sqlid
        if idsql in sql_files:
            r_result.append(idsql)

    return r_result


def argv_parse():
    import sys
    import getopt
    global cluster_t
    global sqllistflag
    global sqlid
    global restflag
    global cleanflag
    sqlid = ""
    global dbfile
    cluster_t = ""
    global appname
    appname = None
    sqllistflag = False
    opts, args = getopt.getopt(sys.argv[1:], "c:s:f:d:", ["rest", "clean", "list", "appname="])

    dbfile = None
    restflag = False
    cleanflag = False
    for op, value in opts:
        if op == "-c":
            cluster_t = value
        elif op == "-s":
            sqlid = value
        elif op == "-f":
            dbfile = value
        elif op == "--rest":
            restflag = True
        elif op == "--clean":
            cleanflag = True
        elif op == "--list":
            sqllistflag = True
        elif op == "--appname":
            appname = value
    if not (sqllistflag or restflag):
        if not appname:
            print "Please --appname=xxx, eg:mq_liruiting_, yq_lisong_"
        if not dbfile:
            print "Please -f db.file to specify dbconfig"
        if not appname or not dbfile:
            exit(-1)


def run():
    argv_parse()
    global sqlid
    global sqlfiles

    sqlfiles = filter_sql_file(path="sql", s_sqlid=sqlid)
    print "All sqls:\n","  \n".join(sqlfiles),"\n---------------"

    global sqllistflag
    if sqllistflag:
        print "Total:", len(sqlfiles)
        return

    global cluster_t

    if restflag:
        get_all_rest()
    else:
        get_database_from_file(dbfile, cluster_t)
        runall()

if __name__ == '__main__':

    # ClusterStr = "bj2,bjcance,chinablood,cmu1h,dili,diri,dlzxyy,dmu1,etyy,fjsl,fybjy,fyyy,gmcah,hbpphosp,hospital302,lnszl,nmgfy,qiluhospital,qyfy,rhab,scmc,sdcancer,sdey,sdhospital,sgyy,shdmu,shfkyypocdemo,shouer,sph,srrsh,syshospital,sysucc,tijmu,tj4thch,uhcmu,xinhuamed,xmzsh,yd2y,ynszlyy,zjyy,zshospital,zxyy"
    all = "agran,bj2,bjcancersouth,bjcancernorth,chinablood,cmu1h,demo,dmu1,etyy,fjsl,fybjy,fyyy,gsyy,gmcah," \
          "hbpphosp,lnszl,motherchildren,nmgfy,pkuph,qiluhospital,qyfy,rhab,scmc,sdcancer,sdey,sdhospital,sgyy,shczyy,shouer,srrsh," \
          "syshospital,sysucc,tijmu,tj4thch,uhcmu,xinhuamed,xmzsh,xnyy,xyhospital,yd2y,ynszlyy,zshospital,zxyy"
    run()
