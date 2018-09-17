#!/usr/bin/env python
#encoding=utf8

import os
import sys
import json
import requests
reload(sys)                         
sys.setdefaultencoding('utf-8') 

def usage():
    print sys.argv[0],'-f <data file>'

if __name__ == "__main__":
    argind = 1
    while argind < len(sys.argv):
        if sys.argv[argind] == "-f":
            file = sys.argv[argind + 1]
            if not os.path.isfile(file):
                print 'input file %s not exist.' % file
                usage()
                exit(1)
            fp = open(file)
            argind += 2
        elif sys.argv[argind] == "-m":
            mapping_file = sys.argv[argind + 1]
            argind += 2
        else:
            print 'unknown option %s' % sys.argv[argind]
            usage()
            exit(1)

    ret = requests.get('http://openapi.intra.yiducloud.cn/openapi/cluster/list')
    data = ret.text
    json_data = json.loads(data)
    value = json_data['value']
    for _id in value:
        cluster_info = value[_id]
        if cluster_info.get('state') == '已上线':
            print cluster_info.get('id')



# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
