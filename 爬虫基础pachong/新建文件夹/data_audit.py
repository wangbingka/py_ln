#!/usr/bin/env python
#encoding=utf8

import os
import sys
import json
import xlrd
import xlwt
import re
import requests
import hashlib
import logger
reload(sys)                         
sys.setdefaultencoding('utf-8') 

def usage():
    print '功能：病历审核工具'
    print 'usage:', sys.argv[0],'options'
    print "options:"
    print '\t-f <data file> : Mandatory, 指定输入文件, 支持excel和文本'
    print '\t-cluster <cluster> : Mandatory, 指定集群'
    print '\t-user <user> : Mandatory, 用户名'
    #print '\t-ext_dict <ext_dict> : Optional, 指定扩展文件，默认为ext.dict'
    print '\t-passwd <passwd> : Mandatory, 密码'
    print '\t-o <output file> : Optional, 指定输出文件, 默认为data_audit_<cluster>.xls'
    print '\t-limit <limit> : Optional, 仅处理前limit条数据, 默认全部'
    print '\t-lb_warning <ratio> : Optional, 下界warning比率，默认0.5'
    print '\t-lb_critical <ratio> : Optional, 下界critical比率，默认0.25'
    print '\t-ub_warning <ratio> : Optional, 上界warning比率，默认2.0'
    print '\t-ub_critical <ratio> : Optional, 上界critical比率，默认4.0'


class QueryParser(object):
    def __init__(self, service_util):
        self.service_util = service_util
        self.op_mapping = {
                '包含' : 'include',
                '不包含' : 'exclude',
                '等于' : 'eq',
                '介于' : 'eq',
                '>=' : 'gte',
                '>' : 'gt',
                '<=' : 'lte',
                '<' : 'lt',
                '=' : 'eq',
                '或者' : 'or',
                'or' : 'or',
                '并且' : 'and',
                'and' : 'and'
                }

    def parse(self, rule, search_aspect=None):
        rule = rule.strip()
        p = re.compile(r'或者|OR|并且|AND')
        m = [ v for v in p.finditer(rule)]
        if len(m) >= 1:
            #AND/OR关系优先级从左到右,从右往左递归
            m = [(v.start(), v.end()) for v in m]
            for (op_start, op_end) in list(reversed(m)):
                op = rule[op_start:op_end].strip().lower()
                right_rule = rule[op_end:]
                left_rule = rule[0:op_start]
                logger.debug('left_rule: %s', left_rule)
                logger.debug('right_rule: %s', right_rule)
                logger.debug('opt: %s', op)
                left_q = self.parse(left_rule)
                right_q = self.parse(right_rule)
                op = self.op_mapping.get(op)
                return {
                        '%s.%s' % (search_aspect, op): [
                            left_q,
                            right_q
                        ]
                    }
        else:
            p = re.compile(r'不包含|包含|等于|>=|>|=|<=|<|介于')
            res = p.findall(rule)
            if len(res) != 1:
                logger.error('invalie rule format :%s', rule)
                raise Exception('invalie rule format :%s' % rule)
            op = res[0].strip().lower()
            key_name = rule.split(op)[0].strip()
            key_value = rule.split(op)[1].strip()
            key_config = self.service_util.lookup_key(key_name)
            op = self.op_mapping.get(op)
            cond =  {
                        'key':key_config.get('key'),
                        'opt':op,
                        'value':key_value
                        }
            if 'unit' in key_config.get('display', {}):
                cond['params'] = dict()
                cond['params']['unit'] = key_config['display']['unit'][0]

            query =  {'condition': cond}
            logger.info('parse, rule:%s, query:%s',rule, json.dumps(query, ensure_ascii=False))
            return query

def genMd5Val(src):
    if not isinstance(src, basestring):
        src = json.dumps(src, ensure_ascii=False, sort_keys=True)

class Rule(object):
    """
    规则
    """
    def __init__(self, service_util, rule, search_aspect, range_lb, range_ub):
        self.service_util = service_util
        self.rule = rule
        if 'search_aspect' == '同病历':
            self.search_aspect = 'visit'
        else:
            self.search_aspect = 'patient'

        self.range_lb = float(range_lb.rstrip('%'))
        self.range_ub = float(range_ub.rstrip('%'))
        self.query_parser = QueryParser(service_util)
        self.parse_rule(rule)

    def parse_rule(self, cond):
        arr = cond.replace('；', ';').split(';')
        if len(arr) != 2:
            logger.error('cond format error: %s', cond)
            raise Exception('cond format error: %s' % cond)
        rule1 = arr[0]
        rule2 = arr[1]
        self.q1 = self.rule_to_query(rule1)
        self.q2 = self.rule_to_query(rule2)
        self.comb_q = {'%s.and' % self.search_aspect: [
                        self.q1,
                        self.q2 
                    ]
                }

    def rule_to_query(self, rule):
        """
        默认对所有rule转换都query都增加日期范围
        """
        q = self.query_parser.parse(rule, self.search_aspect)
        return {'%s.and' % self.search_aspect: [
                        q,
                        {
                            'condition':{
                                'key' : 'visit.admission_time',
                                'op' : 'eq',
                                'value' : '2014-01-01~2017-12-31'
                                }
                        }
                    ]
                }


def genMd5Val(src):
    if not isinstance(src, basestring):
        src = json.dumps(src, ensure_ascii=False, sort_keys=True)
    mobj = hashlib.md5()
    mobj.update(src)
    return mobj.hexdigest()
        
class ServiceUtil(object):
    def __init__(self, cluster, user, passwd, cookies=None):
        self.cluster = cluster
        self.user = user
        self.passwd = passwd
        self.cache = {}
        self.cookies = {}
        self._login(cluster, user, passwd, cookies)

    def _login(self, cluster, user=None, passwd=None, cookies=None):
        cluster_info = self.http_get('http://openapi.intra.yiducloud.cn/openapi/cluster/get?cluster=%s' % cluster)
        self.base_uri = cluster_info.get('value',{}).get('info', {}).get('nova')
        if cookies:
            cookies =  'uid=2b52317cba33-9288-c074-f6a7-f5064ca7; session=fed143604107bb9f2067254915f8391fb980805c85df5dd4692bbefb5f3f9ae977ff832c1c730626b6404a195747a774; sso_usession=fed143604107bb9f2067254915f8391fb980805c85df5dd4692bbefb5f3f9ae977ff832c1c730626b6404a195747a774; osession=232a4736b48f3f7d6419b4c91e3ab8abd27b07ef40213d70ca4df4d3128e6e4b147202c24c51e17bc23eedf988e6a7f7be038b609afd60db1581355bfc3cf9d51ed79bb1545b47354511d13e11fe609deca9c64ab82e55a80b82f63e6a7ee6dc54b4f4c721fcac4f9d68c1a8bcf0110995176d9fd69cc6dba251eeb293fcb69a62da8f3ed25bebc9541b64d523807436f12f4d0606d5f1ac00dc54a80214f86ecad3c7a35374ecbd14549a43edafd0b1f1cad474be7ff61d692e696de2c697a1d493455d28832eceed0ff99434793df035606b3965fd1828ad6257024e7293474d5e30f2b5f94e4e6b46c616fa2a1c07'
            cookies = cookies.split(';')
            for cookie in cookies:
                arr = cookie.split('=')
                self.cookies[arr[0]] = arr[1]
        else:
            url = '%s/sso/passport/user/login' % self.base_uri
            #m = hashlib.md5()
            #m.update(passwd)
            hashed_pwd = genMd5Val(passwd)
            param_dict = {}
	    #param_dict['oauth'] = "http%3A%2F%2F{}%2Fsso%2Foauth%2Ftoken".format(self.host_name)
	    #param_dict['cluster'] = self.cluster_name
	    #param_dict['callback'] = "http%3A%2F%2F{}%2F%23%2Fdata-overview".format(self.host_name)
            param_dict['oauth'] = '%s//sso/oauth/token' % self.base_uri
            param_dict['cluster'] = cluster
            param_dict['callback'] = "%s#/data-overview" % self.base_uri
	    param_dict['appid'] = "79391884-a070-11e4-9ac2-52540f6400b4"
	    ret = requests.post(url, params=param_dict, data={"username": user,
							       "password": hashed_pwd})

	    if ret.status_code == 200:
                print 'login succeed'
		self.cookies = ret.cookies
	    else:
                ret.raise_for_status()
		print 'login failed'
		raise Exception('login failed')


    def login(self, cluster, user, passwd):
        cookies =  'uid=2b52317cba33-9288-c074-f6a7-f5064ca7; session=fed143604107bb9f2067254915f8391fb980805c85df5dd4692bbefb5f3f9ae977ff832c1c730626b6404a195747a774; sso_usession=fed143604107bb9f2067254915f8391fb980805c85df5dd4692bbefb5f3f9ae977ff832c1c730626b6404a195747a774; osession=232a4736b48f3f7d6419b4c91e3ab8abd27b07ef40213d70ca4df4d3128e6e4b147202c24c51e17bc23eedf988e6a7f7be038b609afd60db1581355bfc3cf9d51ed79bb1545b47354511d13e11fe609deca9c64ab82e55a80b82f63e6a7ee6dc54b4f4c721fcac4f9d68c1a8bcf0110995176d9fd69cc6dba251eeb293fcb69a62da8f3ed25bebc9541b64d523807436f12f4d0606d5f1ac00dc54a80214f86ecad3c7a35374ecbd14549a43edafd0b1f1cad474be7ff61d692e696de2c697a1d493455d28832eceed0ff99434793df035606b3965fd1828ad6257024e7293474d5e30f2b5f94e4e6b46c616fa2a1c07'
        cookies = cookies.split(';')
        for cookie in cookies:
            arr = cookie.split('=')
            self.cookies[arr[0]] = arr[1]
        cluster_info = self.http_get('http://openapi.intra.yiducloud.cn/openapi/cluster/get?cluster=%s' % cluster)
        self.base_uri = cluster_info.get('value',{}).get('info', {}).get('nova')
        #self.base_uri = 'http://nova.%s.yiducloud.cn' % cluster

    def http_get(self, uri):
        hash_key = genMd5Val({'uri':uri})
        if hash_key in self.cache:
            return self.cache[hash_key]
        if uri.startswith('http'):
            uri = uri
        else:
            uri = '%s%s' % (self.base_uri, uri)
        ret = requests.get(uri, cookies = self.cookies)
        logger.debug('requests.get, uri:%s, cookies:%s, ret:%s', uri, self.cookies, ret)
        if ret.status_code == 200:
            self.cache[hash_key] = json.loads(ret.text)
            return json.loads(ret.text)
        else:
            ret.raise_for_status()
            raise Exception('http_get failed: %s' % uri)

    def http_post(self, uri, data):
        hash_key = genMd5Val({'uri':uri, 'data':data})
        if hash_key in self.cache:
            return self.cache[hash_key]
        uri = '%s%s' % (self.base_uri, uri)
        data = json.dumps(data)

        headers = {'content-type': 'application/json;charset=utf-8'}
        ret = requests.post(uri, data, cookies = self.cookies, headers = headers)
        logger.debug('requests.post, uri:%s, data:%s, cookies:%s, ret:%s', uri, data, self.cookies, ret)
        if ret.status_code == 200:
            self.cache[hash_key] = json.loads(ret.text)
            return json.loads(ret.text)
        else:
            ret.raise_for_status()

    def lookup_key(self, key_name):
        key_name = key_name.strip()
        res = self.http_get('/api/cg/key/search?aspect=%s.patient&size=30&sug=%s&tag=search' % (self.cluster, key_name))
        res = res.get('value', [])
        if len(res) == 1:
            return res[0]
        elif len(res) > 1:
            #多于一个结果时优先取严格匹配的，没有的话取第一条
            for each in res:
                disp_text = each.get('disp_text', '')
                logger.debug('type(disp_text):%s, disp_text:%s', type(disp_text), disp_text)
                logger.debug('type(key_name):%s, key_name:%s', type(key_name), key_name)
                if disp_text == key_name:
                    logger.debug('more than one key is searched for %s, choose the exact one:%s', key_name, each['key'])
                    return each
            logger.debug('more than one key is searched for %s, choose the first one:%s', key_name, res[0]['key'])
            return res[0]
        else:
            logger.error('failed to search key_name: %s' % key_name)
            raise Exception('failed to search key_name: %s' % key_name)

    def get_patient_cnt(self, cond):
        """获取病人数量"""
        data = {"query": cond}
        #res = self.http_post('/api/query/advance?view=visit&aspect=%s.patient&type=advanced&start=0&size=0' % self.cluster,
        res = self.http_post('/api/shc/hquery/search?view=visit&aspect=%s.patient&type=advanced&start=0&size=0' % self.cluster,
                data)
        return res.get('value', {}).get('patient_num')

class Audit(object):
    def __init__(self, service_util):
        self.service_util = service_util
        self.configs = {'lb_warning':0.5, 'lb_critical':0.25, 'ub_warning':2, 'ub_critical':4}

    def set_config(self, key, value):
        self.configs[key] = value

    def audit(self, rule):
        logger.info('rule.q1:', rule.q1)
        logger.info('rule.q2:', rule.q2)
        logger.info('rule.comb_q:', rule.comb_q)
        patient_num1 = service_util.get_patient_cnt(rule.q1)
        patient_num2 = service_util.get_patient_cnt(rule.q2)
        patient_num_comb = service_util.get_patient_cnt(rule.comb_q)
        if patient_num1 == 0:
            ratio = 0.0
        else:
            ratio = float(patient_num_comb) / patient_num1

        result = 'PASS'

        if ratio < rule.range_lb * float(self.configs['lb_critical']) or ratio > rule.range_ub * float(self.configs['ub_critical']):
            result = 'CRITICAL'
        elif ratio < rule.range_lb * float(self.configs['lb_warning']) or ratio > rule.range_ub * float(self.configs['ub_warning']):
            result = 'WARNING'
        elif ratio < rule.range_lb or ratio > rule.range_ub:
            result = 'CHECK'
      
        """
        print '%s\t%s\t%s\t%d\t%d\t%d\t%.02f\t%.02f\t%.02f\t%s' % (rule,
                                        rule.range_lb,
                                        rule.range_ub,
                                        patient_num1, 
                                        patient_num2, 
                                        patient_num_comb,
                                        ratio,
                                        rule.range_lb,
                                        rule.range_ub,
                                        result
                                        )
        """
        return {'patient_num1': patient_num1,
                'patient_num2': patient_num2,
                'patient_num_comb': patient_num_comb,
                'ratio': ratio,
                'result': result
                }

class CondExtender(object):
    """
    扩展器，把特殊字符串做替换
    """
    def __init__(self, ext_dict_file=None, ext_data=None):
        self.ext_dict = {}
        self.dict_file = ext_dict_file
        self.load(self.dict_file, ext_data)

    def load(self, ext_dict_file=None, ext_data=None):
        if ext_dict_file and os.path.isfile(ext_dict_file):
            ext_data = open(ext_dict_file)
        if ext_data is None:
            return
        for line in ext_data:
            line = line.rstrip('\n')
            arr = line.split('\t')
            arr = [v.strip() for v in arr]
            if arr[0] not in self.ext_dict:
                self.ext_dict[arr[0]] = [arr[1]]
            else:
                self.ext_dict[arr[0]].append(arr[1])

    def extend(self, rule):
        rule = rule.strip()
        p = re.compile(r'##')
        m = [ v for v in p.finditer(rule)]
        if len(m) != 2:
            return [rule]
        res = []
        left_text = rule[0:m[0].start()]
        right_text = rule[m[1].end():]
        ext_key = rule[m[0].end():m[1].start()]
        if ext_key in self.ext_dict:
            ext_values = self.ext_dict[ext_key]
            for ext_value in ext_values:
                res.append('%s%s%s' % (left_text, ext_value, right_text))
        else:
            logger.error('ext_key %s not found in dict file %s', ext_key, self.dict_file)
            raise Exception('ext_key %s not found in dict file %s' % (ext_key, self.dict_file))

        return res

class ExcelWriter(object):
    def __init__(self):
        self.book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        self.sheet = self.book.add_sheet(u'执行结果', cell_overwrite_ok=True)
        self.nrows = 0

    def write_row(self, data):
        if not isinstance(data, list):
            return
        for i in range(len(data)):
            self.sheet.write(self.nrows, i, data[i])
        self.nrows += 1

    def save(self, filename):
        self.book.save(filename)


if __name__ == "__main__":
    argind = 1
    #logger.setup_logger()
    cluster = None
    user = None
    passwd = None
    cookies =  'uid=2b52317cba33-9288-c074-f6a7-f5064ca7; session=fed143604107bb9f2067254915f8391fb980805c85df5dd4692bbefb5f3f9ae977ff832c1c730626b6404a195747a774; sso_usession=fed143604107bb9f2067254915f8391fb980805c85df5dd4692bbefb5f3f9ae977ff832c1c730626b6404a195747a774; osession=232a4736b48f3f7d6419b4c91e3ab8abd27b07ef40213d70ca4df4d3128e6e4b147202c24c51e17bc23eedf988e6a7f7be038b609afd60db1581355bfc3cf9d51ed79bb1545b47354511d13e11fe609deca9c64ab82e55a80b82f63e6a7ee6dc54b4f4c721fcac4f9d68c1a8bcf0110995176d9fd69cc6dba251eeb293fcb69a62da8f3ed25bebc9541b64d523807436f12f4d0606d5f1ac00dc54a80214f86ecad3c7a35374ecbd14549a43edafd0b1f1cad474be7ff61d692e696de2c697a1d493455d28832eceed0ff99434793df035606b3965fd1828ad6257024e7293474d5e30f2b5f94e4e6b46c616fa2a1c07'
    cookies = None
    ext_dict = None
    ext_data = []
    output_file = None
    limit = -1
    configs = {}
    while argind < len(sys.argv):
        if sys.argv[argind] == "-f":
            file = sys.argv[argind + 1]
            if not os.path.isfile(file):
                print 'input file %s not exist.' % file
                usage()
                exit(1)
            argind += 2
        elif sys.argv[argind] == "-cluster":
            cluster = sys.argv[argind + 1]
            argind += 2
        elif sys.argv[argind] in ["-o", "-output"]:
            output_file = sys.argv[argind + 1]
            argind += 2
        elif sys.argv[argind] == "-user":
            user = sys.argv[argind + 1]
            argind += 2
        elif sys.argv[argind] == "-passwd":
            passwd = sys.argv[argind + 1]
            argind += 2
        elif sys.argv[argind] == "-cookies":
            cookies = sys.argv[argind + 1]
            argind += 2
        elif sys.argv[argind] == "-limit":
            limit = int(sys.argv[argind + 1])
            argind += 2
        elif sys.argv[argind] == "-ext_dict":
            ext_dict = sys.argv[argind + 1]
            argind += 2
        elif sys.argv[argind] in ["-lb_warning", "-ub_warning", "-lb_critical", "-ub_critical"]:
            configs[sys.argv[argind].lstrip('-')] = sys.argv[argind + 1]
            argind += 2
        elif sys.argv[argind] == "-debug":
            logger.set_debug()
            argind += 1
        else:
            print 'unknown option %s' % sys.argv[argind]
            usage()
            exit(1)

    if cookies is None and user is None and passwd is None:
        print 'error: either cookies or user&passwd must be given'
        exit(1)

    if cluster is None:
        print 'cluster must be specified'
        exit(1)

    if not os.path.isfile(file):
        print '%s is not a file' % file
        exit(1)

    fp = []
    header_lines = 0
    if 'xls' in file:
        header_lines = 2
        book = xlrd.open_workbook(file)
        sheet_rule = book.sheet_by_name(u'执行全表')
        nrows = sheet_rule.nrows
        for i in range(1, nrows):
            row_values = [str(v) for v in sheet_rule.row_values(i)]
            fp.append('\t'.join(row_values))
        
        if not ext_dict:
            sheet_ext = book.sheet_by_name(u'扩展词表')
            nrows = sheet_ext.nrows
            for i in range(1, nrows):
                row_values = [str(v) for v in sheet_ext.row_values(i)]
                ext_data.append('\t'.join(row_values))
    else:
        fp = open(file)

    cond_extender = CondExtender(ext_dict, ext_data)
    service_util = ServiceUtil(cluster, user, passwd, cookies)
    auditor = Audit(service_util)
    for config_key in configs:
        auditor.set_config(config_key, configs[config_key])

    #输出Excel表头
    if output_file is None:
        output_file = 'data_audit_%s.xls' % cluster
    excel_writer = ExcelWriter()
    excel_writer.write_row(['', '', '规则', '范围下界', '范围上界', \
            '搜索纬度', 
            'patient_num1', 
            'patient_num2', 
            'patient_num_both', 
            'ratio',
            'result'
            ])

    index = 0
    for line in fp[0:limit]:
        index += 1
        print 'line: %d' % index
        line = line.rstrip()
        if line.startswith('#'):
            continue
        arr = line.split('\t')
        #if index <= header_lines:
        #    excel_writer.write_row(arr)
        #    continue

        #要求第2，3，4，6列必须全非空
        if len(arr) < 6 or not all(arr[2:6]):
            excel_writer.write_row(arr)
            continue

        cond = arr[2]
        audit_lb = arr[3]
        audit_ub = arr[4]
        aspect = arr[5]
        extended_cond = cond_extender.extend(cond)
        for each_cond in extended_cond:
            try:
                rule = Rule(service_util, each_cond, aspect, audit_lb, audit_ub)
                ret = auditor.audit(rule)
                data = '%s\t%s\t%s\t%s\t%s\t%s\t%d\t%d\t%d\t%.02f\t%s' % (
                                                arr[0],
                                                arr[1],
                                                each_cond,
                                                audit_lb,
                                                audit_ub,
                                                aspect,
                                                ret.get('patient_num1'), 
                                                ret.get('patient_num2'), 
                                                ret.get('patient_num_comb'),
                                                ret.get('ratio'),
                                                ret.get('result')
                                                )
                print data
                excel_writer.write_row(data.split('\t'))
            except Exception as e:
                sys.stderr.write('exception when handle rule:%s, exception: %s\n' % (each_cond, e))
                data = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (
                                                arr[0],
                                                arr[1],
                                                each_cond,
                                                audit_lb,
                                                audit_ub,
                                                aspect,
                                                'NA',
                                                'NA',
                                                'NA',
                                                'NA',
                                                'Exception:%s' % e
                                                )
                print data
                excel_writer.write_row(data.split('\t'))
        
        excel_writer.save(output_file)
# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
