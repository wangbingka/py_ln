#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/5 16:19
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

# names = locals()
# for i in range(1,2):
#     names['a%i'%i] = input('Abss %d:'%i)
# for i in range(1,2):
#     print(names['a%i'%i])


import json
import hashlib

def gen_md5(self):
    if not self:
        return None
    m1 = hashlib.md5()
    m1.update(self.encode("utf8"))
    return m1.hexdigest()
def genMd5Val(src):
    if not isinstance(src, str):
        src = json.dumps(src, ensure_ascii=False, sort_keys=True)
    mobj = hashlib.md5()
    mobj.update(src.encode("utf8"))
    return mobj.hexdigest()

str1 = "你好"
print(str1)
print (json.dumps(str1,ensure_ascii=False))

import requests

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
'Connection':'keep-alive',}

session = requests.session()
session.headers.update(headers)

nginx_proxy_session = "Zm8M0XNiBixi8GjB3wRgWg..|1537323095|2OXyzeqpQIOY2RQtrjBwsRpiWF0." # 每日更新
requests.utils.add_dict_to_cookiejar(session.cookies,{"nginx_proxy_session":nginx_proxy_session})

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
        # print(cluster_info)
        print(self.base_uri)
        if cookies:
            print(cookies)
            cookies =  'uid=2b52317cba33-9288-c074-f6a7-f5064ca7; session=fed143604107bb9f2067254915f8391fb980805c85df5dd4692bbefb5f3f9ae977ff832c1c730626b6404a195747a774; sso_usession=fed143604107bb9f2067254915f8391fb980805c85df5dd4692bbefb5f3f9ae977ff832c1c730626b6404a195747a774; osession=232a4736b48f3f7d6419b4c91e3ab8abd27b07ef40213d70ca4df4d3128e6e4b147202c24c51e17bc23eedf988e6a7f7be038b609afd60db1581355bfc3cf9d51ed79bb1545b47354511d13e11fe609deca9c64ab82e55a80b82f63e6a7ee6dc54b4f4c721fcac4f9d68c1a8bcf0110995176d9fd69cc6dba251eeb293fcb69a62da8f3ed25bebc9541b64d523807436f12f4d0606d5f1ac00dc54a80214f86ecad3c7a35374ecbd14549a43edafd0b1f1cad474be7ff61d692e696de2c697a1d493455d28832eceed0ff99434793df035606b3965fd1828ad6257024e7293474d5e30f2b5f94e4e6b46c616fa2a1c07;nginx_proxy_session=Zm8M0XNiBixi8GjB3wRgWg..|1537323095|2OXyzeqpQIOY2RQtrjBwsRpiWF0.'
            cookies = cookies.split(';')
            for cookie in cookies:
                arr = cookie.split('=')
                self.cookies[arr[0]] = arr[1]
        else:
            url = '%s/sso/passport/user/login' % self.base_uri
            print(url)
            #m = hashlib.md5()
            #m.update(passwd)
            hashed_pwd = genMd5Val(passwd)
            print(hashed_pwd)
            param_dict = {}
            #param_dict['oauth'] = "http%3A%2F%2F{}%2Fsso%2Foauth%2Ftoken".format(self.host_name)
            #param_dict['cluster'] = self.cluster_name
            #param_dict['callback'] = "http%3A%2F%2F{}%2F%23%2Fdata-overview".format(self.host_name)
            param_dict['oauth'] = '%s/sso/oauth/token' % self.base_uri
            param_dict['cluster'] = cluster
            param_dict['callback'] = "%s#/data-overview" % self.base_uri
            param_dict['appid'] = "79391884-a070-11e4-9ac2-52540f6400b4"

        print(param_dict)
        print({"username": user,"password": hashed_pwd})
        print(json.dumps({"username": user,"password": hashed_pwd}))
        ret = session.post(url, params=param_dict, data=json.dumps({"username": user,
							       "password": hashed_pwd}))
        print(ret)
        print(ret.text)
        if ret.status_code == 200:
            print(ret.text)
            print('login succeed')
            self.cookies = ret.cookies
        else:
            # ret.raise_for_status()
            print('login failed')
            # raise Exception('login failed')


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
        print('uri:%s'%uri)
        hash_key = genMd5Val({'uri':uri})
        print(hash_key)
        if hash_key in self.cache:
            return self.cache[hash_key]
        if uri.startswith('http'):
            uri = uri
        else:
            uri = '%s%s' % (self.base_uri, uri)
        ret = requests.get(uri, cookies = self.cookies)
        # logger.debug('requests.get, uri:%s, cookies:%s, ret:%s', uri, self.cookies, ret)
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
        ret = session.post(uri, data, cookies = self.cookies, headers = headers)
        print(ret)
        print(ret.text)
        # logger.debug('requests.post, uri:%s, data:%s, cookies:%s, ret:%s', uri, data, self.cookies, ret)
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
                pass
                # logger.debug('type(disp_text):%s, disp_text:%s', type(disp_text), disp_text)
                # logger.debug('type(key_name):%s, key_name:%s', type(key_name), key_name)
                if disp_text == key_name:
                    pass
                    # logger.debug('more than one key is searched for %s, choose the exact one:%s', key_name, each['key'])
                    return each
            # logger.debug('more than one key is searched for %s, choose the first one:%s', key_name, res[0]['key'])
            return res[0]
        else:
            # logger.error('failed to search key_name: %s' % key_name)
            raise Exception('failed to search key_name: %s' % key_name)

    def get_patient_cnt(self, cond):
        """获取病人数量"""
        data = {"query": cond}
        #res = self.http_post('/api/query/advance?view=visit&aspect=%s.patient&type=advanced&start=0&size=0' % self.cluster,
        res = self.http_post('/api/shc/hquery/search?view=visit&aspect=%s.patient&type=advanced&start=0&size=0' % self.cluster,
                data)
        return res.get('value', {}).get('patient_num')

if __name__ == '__main__':
    a = ServiceUtil('fjsl','wangbingka@yiducloud','*****')