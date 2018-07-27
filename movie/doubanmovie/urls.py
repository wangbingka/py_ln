"""doubanmovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
客户端，常见的是浏览器，输入电影名
    点击搜索，是在发出一种请求
到服务器段，web应用
    1、服务器端收到客户端的请求内容
    2、查询表格，或者数据库，exce;,mysql等
    3、获取表格信息，查询过程
    4、返回查询到的数据，发还给客户端
客户端收到服务器发回的数据，一次服务完成
常用框架 django
"""


from django.contrib import admin
from django.urls import include, path


#python manage.py startproject projectName ,新建一个项目
#python manage.py startapp appName，要在项目目录下新建模块
#python manage.py runserver 运行这个服务器起来
#python manage.py makemigrations ，执行数据
#python manage.py migrate，数据库层面改动数据操作

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls')),
]

#http://127.0.0.1:8000/movie/,网址栏首先输入这一个，然后根据后面的urls内容继续往后输入

#何时使用 include(),当包括其它 URL 模式时你应该总是使用 include() ， admin.site.urls 是唯一例外。
#通过前面的'admin'或者'movie'，进入一个界面，除非是admin.site.urls，其他都应该用include来引导

