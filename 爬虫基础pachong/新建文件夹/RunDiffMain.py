#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author: tingru.yin@yiducloud.cn, 2017, all rights reserved
#@Created on 2017-06-07
#@Brief:

__author__ = 'yintingru'
from XlsEngine import  XlsEngine_wt
import DataEngine
import ConfigParser,time,Logging
import sys
import json
import urllib2
import requests
from Request import Request
from Login import Login
reload(sys)
sys.setdefaultencoding( "utf-8" )
import xlrd
xlrd.Book.encoding="utf-8"
import HttpService


DATE=time.strftime(r'%Y-%m-%d-%H%M%S', time.localtime(time.time()))
username = "yintingru@yiducloud"
password = "Yintingru1129"

                           #读取VIP测试接口IP

#Excel的sheet中只保存同一接口的用例参数，不同接口保存在不同sheet中，通过修改sheet索引，获取不同接口的参数列表
dataList0=DataEngine.data2List("./DataSrc/diffCase.xlsx",0)#简单搜索case
dataList1=DataEngine.data2List("./DataSrc/diffCase.xlsx",1)#高级搜索case
dataList2=DataEngine.data2List("./DataSrc/diffCase.xlsx",2)#科研搜索case
dataList3=DataEngine.data2List("./DataSrc/diffCase.xlsx",3)#简单搜索权限case
dataList4=DataEngine.data2List("./DataSrc/diffCase.xlsx",4)#高级搜索权限case
dataList5=DataEngine.data2List("./DataSrc/diffCase.xlsx",5)#科研搜索权限case
#Service2_dataList=DataEngine.data2List(r'.\DataSrc\dataCase.xls',2)
datadict={"0":"简单搜索核心case",
"1":"高级搜索核心case",
"2":"科研搜索核心case",
"3":"简单搜索权限case",
"4":"高级搜索权限case",
"5":"科研搜索权限case"
}

def get_cluster_str():
    url = "http://openapi.intra.yiducloud.cn/openapi/cluster/list"
    r = requests.get(url=url)
    clusterstr = ""
    hosplist = ""
    count = 0
    for x in r.json()['value'].values():
            # print " %(name)s %(id)s |"%x
        clusterstr +=x['id']+','
        hosplist += " %(name)s %(id)s |"%x
        count +=1

    return clusterstr.rstrip(',')

def output_print(result_output,all,right_num,error_num):

    print "all number:",all,"|","right_num:",right_num,"error_num:",error_num,"succuss rate:",float(right_num)/all*100,"%\n"
    for i in range(len(result_output)):
        output= str(result_output[i]["i"])+")"+"\t|\t"+str(result_output[i]["result"])+"\t|\t"+result_output[i]["check"].encode('utf-8')
        if "error" in result_output[i].keys():
            output=output+ "\t|\t"+ str(result_output[i]["error"]).encode("utf-8")
        if "username" in result_output[i].keys():
            output=output+ "\t|\t"+ str(result_output[i]["username"])
        print output

def runTest(datalist,cluster,xlw,conf):
    result_output=[]
    all=len(datalist)
    right=0
    error=0
    funname=eval("HttpService.requrl_%s" %conf)
    DataEngine.setrow(1)
    for i in range(len(datalist)):
        try:
            previewtarget = "preview"
            prodtarget = "prod"
            try:
                reqpreview,reqjson1=funname(datalist[i],cluster,previewtarget)
            except urllib2.URLError,e:
                DataEngine.resulterror(str(e.code) + "preview", xlw, datalist, i, str(datalist[i][10]))
                raise

            try:
                reqprod,reqjson2=funname(datalist[i],cluster,prodtarget)
            except urllib2.URLError, e:
                DataEngine.resulterror(str(e.code) + "prod", xlw, datalist, i, str(datalist[i][10]))
                raise

            result,result_list = DataEngine.resultDiff(reqpreview,reqprod,xlw,datalist,i,str(datalist[i][10]),reqjson1["url"])
            if result:
                right=right+1
                dict={"i":i,"result":result,"check":datalist[i][2]}
                result_output.append(dict)
            else:
                error=error+1
                dict = {"i": i, "result": result, "check": datalist[i][2],"error":result_list,"username":datalist[i][4]}
                result_output.append(dict)
        except Exception,e:
            #print(str(list[i][1])+"\t"+str(e))
            #Logging.writeException(e)
            print "Exception：",e
            error=error+1
            dict = {"i": i, "result": "error but don't know the error type", "check": datalist[i][2], "error": e,"username":datalist[i][4]}
            result_output.append(dict)
            DataEngine.resulterror(e, xlw, datalist, i, str(datalist[i][10]))
    print "~~~~~~~~~~~~~"+cluster+"~~~~~~~~~~~~~~~~~~~~~~~"
    output_print(result_output,all,right,error)

def get_argv():
    """
    命令行参数解析
    :return:
    """
    import getopt
    import sys
    opts, args = getopt.getopt(sys.argv[1:], "c:s:")
    global cluster
    global target
    global sheet
    for op, value in opts:
        if op == "-c":
            cluster = value
        elif op == "-s":
            sheet = value
    if cluster=="all":
        cluster=get_cluster_str()

    # debug code
    print "----- argv list ------"
    print "医院", cluster
    print "sheet case",sheet
    #print "环境", target

def run():
    print "start"
    get_argv()
    #sheet='5'
    #cluster='lnszl,tijmu,yd2y,fyyy,tj4thch,fybjy,chinablood,etyy,xnyy,xyhospital,hbpphosp,zxyy,sdey,gmcah,bj2,sgyy,nmgfy,qyfy,sdcancer,syshospital,scmc,shouer,sdhospital,ynszlyy,xinhuamed,fjsl,qiluhospital,bjcancer,cmu1h,xmzsh'
    cluster_list=cluster.split(",")
    sheet_list=sheet.split(",")
    xlw = XlsEngine_wt(r'./ResultReport/'+DATE+'diff.xls')
    for j in range(len(cluster_list)):
        print "\n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~[START RUN] "+cluster_list[j]+"~~~~~~~~~~~~~~~~~~~"
        print "\n"
        for i in range(len(sheet_list)):
            xlw.add_sheet("result"+sheet_list[i])
            print "～～～～～～～～～～～～start run sheet" + datadict[str(sheet_list[i])]+"\tcluster:"+cluster_list[j]+"～～～～～～～～～～～～～～～"
            if sheet_list[i]=="2" or sheet_list[i]=="5":
                runTest(eval("dataList" + sheet_list[i]),cluster_list[j],xlw,"keyan")
            else:
                runTest(eval("dataList" + sheet_list[i]),cluster_list[j],xlw,"simple")

    xlw.save_xls()
    print "end"

if __name__ == '__main__':
    run()
