#!usr/bin/python
#coding:utf-8
#author:bingka.wang

from html.parser import HTMLParser

'''
1.HTMLParser主要是用来解析HTML文件（包括HTML中无效的标记）
2.参数convert_charrefs表示是否将所有的字符引用自动转化为Unicode形式，Python3.5以后默认是True
3.HTMLParser可以接收相应的HTML内容，并进行解析，遇到HTML的标签会自动调用相应的handler（处理方法）来处理，用户需要自己创建相应的子类来继承HTMLParser，并且复写相应的handler方法
4.HTMLParser不会检查开始标签和结束标签是否是一对
'''

'''
1.HTMLParser.feed(data)：接收一个字符串类型的HTML内容，并进行解析
2.HTMLParser.close()：当遇到文件结束标签后进行的处理方法。如果子类要复写该方法，需要首先调用HTMLParser累的close()
3.HTMLParser.reset():重置HTMLParser实例，该方法会丢掉未处理的html内容
4.HTMLParser.getpos()：返回当前行和相应的偏移量
5.HTMLParser.handle_starttag(tag, attrs)：对开始标签的处理方法。例如<div id="main">，参数tag指的是div，attrs指的是一个（name,Value)的列表
6.HTMLParser.handle_endtag(tag)：对结束标签的处理方法。例如</div>，参数tag指的是div
7.HTMLParser.handle_data(data)：对标签之间的数据的处理方法。<tag>test</tag>,data指的是“test”
8.HTMLParser.handle_comment(data)：对HTML中注释的处理方法。

'''
class MyHTMLParser(HTMLParser):
    a_t = False
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        if str(tag).startswith("title"):
            self.a_t = True

    # 根据某些条件，获取data值
    def handle_data(self, data):
        if self.a_t is True:
            print("得到的数据: ",data)

    #打印所有的data值
    def handle_data(self, data):
        print("Encountered some data  :", data)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)



parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>''<body><h1>Parse me!</h1></body></html>')