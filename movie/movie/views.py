from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request,name):
    #name是需要在网址中输入的内容，可以随便输入

    #获取要查询的电影
    movie = name
    print(movie)
    #打开excel,数据存储库
    lines = ['蛮荒故事 Relates salvajes','肖申克的救赎 Relates salvajes']

    #查询
    for line in lines:
        if movie in line:
            # return HttpResponse(line)
            context = {'tip': line,'sayhi': 'hello!'}
            return render(request, 'movie/index.html', context)
    fo =  'for'

    #传递变量，可以一次传递多个变量
    """
    1、index.html中使用方式： {{ tip }}
    2、如果变量不多，可以直接放入render作为第三个参数
       
    """
    # context = }
    # return render(request, 'movie/index.html', context)

    return render(request, 'movie/index.html', {'tip': '没有该电影', 'sayhi': '很遗憾，我们会尽快添加！'})

    # 怎么使用html文件
    """
    1、如果需要运行html,必须把建立的app，加入setting.py的‘NSTALLED_APPS’列表中
    2、在app下面，建立templates文件夹，直接放，直接只用'index.html',或者继续加子目录，前面就需要加上路径
    
    """


# orm，可以数据映射不同类型的数据库，包括sqlite,mysql,oracal
