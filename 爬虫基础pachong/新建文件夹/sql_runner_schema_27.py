# -*- coding: UTF-8 -*-
'''
 * Created by yangfan on 2018/03/08.
'''
import requests
import time
import os
ENCODING = 'utf-8'
USER = "fan.yang"
TOKEN = "3caa315fcff93e6137f5c37eb920e204"
result = {}
_result = {}
PWD = "Fany.810818"
AZ_HOST = "http://azkaban.intra.yiducloud.cn/azkaban-proxy"
INTERVAL = 10


def get_target_database(cluster, type='etldr', product='nova'):
    database = "" if not cleanflag else "clean"
    hulk_url = 'http://hulk.m.com/api/hulk/database/getlatest'
    parames = {"type": type,
                "hospital_code": cluster,
                 "product":product}
    rsp = requests.get(url=hulk_url, params=parames, timeout=200)
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


def get_database_from_file(filepath='etldb.txt'):
    print "get db from",filepath
    clean = "" if not cleanflag else "clean"
    n = 0
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            # print "line",line
            linedata = line.split()
            if not linedata or line.startswith('#'):
                continue
            cluster = linedata[0]
            dbname = linedata[1]
            result[cluster] = {'database': "%s%s" % (dbname, clean)}
            n += 1
            # print n, cluster, dbname
    print "-------------------------------"


def request_az(rdata):
    az_url = AZ_HOST + '/schedule'
    result = None
    try:
        response = requests.post(url=az_url, data=rdata, timeout=100)
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


def get_executor_data(cluster):
    print "cluster:",cluster,
    database = result[cluster].get('database')
    if database is None:
        database = get_target_database(cluster)
    print "database:", database
    if database == '':
        print cluster, "no database."
        exit(-1)

    with open(sqlfile) as f:

        sql = f.read()
        import chardet
        print sqlfile, chardet.detect(sql)
        sql2 = sql.decode('utf-8').replace('%s', database).replace('\n','').replace('\r','')
        print "sql2",type(sql2)

    print "sql2:", sql2.encode(ENCODING)
    #cdata = "cluster=qyfy&method=run&user=fan.yang&token=7f722bbb7fab53b82c14bb9141f96192&jobType=sql_executor&jobParams={\"input\":\"-n default -s testsql -t local -f /user/data/etldr/test \"}&jobFiles={\"file\":'select * from qyfy_20171026_200_2_etldr.tbl_adt_admits_discharges a limit 1;'}"
    rdata = {
        "cluster": cluster,
        "method": "run",
        "user": USER,
        "token": TOKEN,
        "jobType": "sql_executor",
        "jobParams": "{\"input\": \"-p %s -n default -s testsql -t local -f /user/data/etldr/test \"}" % PWD,
        # "jobFiles": "{\"file\":'%s'}" % sql2.decode("unicode-escape")
        "jobFiles": "{\"file\":\"%s\"}" % sql2
    }
    print "executor request data:", rdata
    resp = request_az(rdata)
    project = ""
    execid = ""
    print "resp",resp
    if resp:
        project = resp.get('project')
        execid = resp.get('execid')
    print  "cluster:",cluster," project:", project, " execid:", execid
    result[cluster]['project']=project
    result[cluster]['execid']=execid
    return project, execid


def get_hive_excutor_job(cluster):
    print "cluster:",cluster,
    database = result[cluster].get('database')
    if database is None:
        database = get_target_database(cluster)
    print "database:", database
    if database == '':
        print cluster, "no database."
        exit(-1)

    with open(sqlfile) as f:

        sql = f.read()
        import chardet
        print sqlfile, chardet.detect(sql)
        sql2 = sql.decode('utf-8').replace('%s', database).replace('\n','').replace('\r','').replace('\"', '\'')
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
    print  "cluster:",cluster," project:", project, " execid:", execid
    result[cluster]['project']=project
    result[cluster]['execid']=execid
    return project, execid


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
    print "\n-------- start on %s --------\n" % cluster
    project, execid = get_hive_excutor_job(cluster)
    time.sleep(10)
    status = get_exec_status(cluster, project, execid)
    retry = 1
    _rerty = retry

    while (status == 'RUNNING' or status == 'PREPARING') and retry > 0:
        time.sleep(60)
        status = get_exec_status(cluster, project, execid)
        print cluster,"exec status:", status
        retry -= 1
    if retry == 0 and status != 'SUCCEEDED':
        print "[WARN]After  secondes. Cluster: %s, status: %s" % (cluster, status)

    result[cluster]['status'] = status
    print cluster, 'status:',status
    if status == 'SUCCEEDED':
        r = get_query_data(cluster, project)
        print cluster,"SQL Result:",r,"Convert format:",convert_unicode(r)
        if r:
            data = r.get('data')
        else:
            result[cluster]['status'] = "RUNNING"
        result[cluster]['data']= data
    generate_result(cluster)
    print "\n-------- end on %s --------\n" % cluster


def runall():
    global result
    if not dbfile:
        print "Please -f db.file to specify dbconfig"
        exit(0)
    get_database_from_file(dbfile)

    if cluster_t:
        clusters = cluster_t.split(',')
        t_result = {}

        for cluster in clusters:
            if cluster in result:
                t_result[cluster] = result[cluster]

        result = t_result
    cluster_list = result.keys()
    for n, cluster in enumerate(cluster_list):
        database = result[cluster].get('database')
        print n+1, cluster, database

    import threading
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
    show_rest()


def generate_result(cluster):

    if cluster not in result:
        return

    data = result[cluster].get('data',"")
    status = result[cluster]['status']
    if status == 'SUCCEEDED':
        filename = "result/%s_%s_%s.txt" % (sqlid, cluster, result[cluster]['database'])
        with open(filename, 'w') as f:
            f.write(data.encode(ENCODING))


def show_rest(result1=None):
    if result1 is None:
        result1 = result
    rows = ""

    for cluster in result1.keys():
        # name = clusterdict.get(cluster,'')
        data = result1[cluster].get('data',"")
        if not data:
            status = result1[cluster].get('status')
            project = result1[cluster].get('project')
            execid = result1[cluster].get('execid')
            database = result1[cluster].get('database')
            row = "%s\t%s\t%s\t%s\t%s\n" % (cluster, database, status, project, execid)
            print "show_rest:", row
            rows += row
    if rows:
        with open('rest/%s_rest.txt' % sqlid, 'aw+') as f:
            f.write(rows.encode(ENCODING))


def get_rest_data(filepath='rest/rest.txt'):
    update_rest = ""
    with open(filepath, 'r') as f:
        for line in f.readlines():
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
            # print "cluster:database:project:execid:old-status", cluster, database, project, execid, status
            if status != 'FAILED' and status != 'Skip' and status != 'SUCCEEDED':
                #再次取查询数据
                status = get_exec_status(cluster, project, execid)
                print cluster, "exec status:", status
                if status == 'SUCCEEDED':
                    result[cluster]['status'] = status
                    r = get_query_data(cluster, project)
                    print cluster, "SQL Result:", r, "Convert format:", convert_unicode(r)
                    if 'warn' in r:
                        print r['warn']
                    else:
                        data = r['data']
                        result[cluster]['data'] = data
                        generate_result(cluster)

            if status != 'SUCCEEDED':
                nline = "%s\t%s\t%s\t%s\t%s\n" % (cluster, database, status, project, execid)
            else:
                nline = "#%s\t%s\t%s\t%s\t%s\n" % (cluster, database, status, project, execid)
                print nline
            update_rest += "%s" % nline
    import os
    os.rename(filepath, "%s.bak" % filepath)
    with open('rest/%s_rest.txt' % sqlid, 'aw') as fw:
        print "update rest/%s_rest.txt" % sqlid
        fw.write(update_rest.encode(ENCODING))


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
        if file.startswith('R0') and file.endswith('.sql'):
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
    global sqlfile
    global sqlid
    global restflag
    global cleanflag
    sqlid = ""
    global dbfile
    global resultflag
    cluster_t = ""
    sqllistflag = False
    opts, args = getopt.getopt(sys.argv[1:], "c:s:f:d:", ["rest", "clean", "list", "result"])

    dbfile = "etl.txt"
    restflag = False
    cleanflag = False
    resultflag = False
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
        elif op == "--result":
            resultflag = True


def run():
    argv_parse()
    global sqlid
    global sqllistflag
    global restflag
    global resultflag
    sqlfiles = filter_sql_file(s_sqlid=sqlid)
    print "All sqls:\n", "  \n".join(sqlfiles), "\n---------------"
    if not restflag and sqllistflag:
        print "Total:", len(sqlfiles)
        return

    lackrest = []
    for sqlid in sqlfiles:
        if restflag :
            restfile = 'rest/%s_rest.txt'% sqlid
            isrestexist = os.path.exists(restfile)
            if isrestexist and not sqllistflag:
                # print "Get result from", restfile
                get_rest_data(restfile)
            elif not isrestexist:
                _sqlid = sqlid.replace(".sql", "")
                # print sqlid
                # if " " in sqlid:
                #     print "sqlid",sqlid
                lackrest.append(_sqlid)
                # print "%s not exitsts.SKIP" % restfile

        else:

            global sqlfile
            sqldir = 'sql/'
            sqlfile = os.path.join(sqldir, sqlid)
            print "Start", sqlfile
            runall()

        if resultflag:
            resultfile = 'result/%s_xinhuamed_20170901_32_3_schema.txt' % sqlid
            isresultexist = os.path.exists(resultfile)
            if not isresultexist:
                print resultfile, "result not exits"

    if restflag and sqllistflag:
        pass
        print "Following sqls has no rest file:"
        print ",".join(lackrest)
        print "Total:", len(lackrest)

if __name__ == '__main__':

    # ClusterStr = "bj2,bjcance,chinablood,cmu1h,dili,diri,dlzxyy,dmu1,etyy,fjsl,fybjy,fyyy,gmcah,hbpphosp,hospital302,lnszl,nmgfy,qiluhospital,qyfy,rhab,scmc,sdcancer,sdey,sdhospital,sgyy,shdmu,shfkyypocdemo,shouer,sph,srrsh,syshospital,sysucc,tijmu,tj4thch,uhcmu,xinhuamed,xmzsh,yd2y,ynszlyy,zjyy,zshospital,zxyy"
    all = "agran,bj2,bjcancersouth,bjcancernorth,chinablood,cmu1h,demo,dmu1,etyy,fjsl,fybjy,fyyy,gsyy,gmcah," \
          "hbpphosp,lnszl,motherchildren,nmgfy,pkuph,qiluhospital,qyfy,rhab,scmc,sdcancer,sdey,sdhospital,sgyy,shczyy,shouer,srrsh," \
          "syshospital,sysucc,tijmu,tj4thch,uhcmu,xinhuamed,xmzsh,xnyy,xyhospital,yd2y,ynszlyy,zshospital,zxyy"
    run()
