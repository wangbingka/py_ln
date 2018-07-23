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
from django.contrib import admin
from django.urls import include, path

#python manage.py startproject projectName ,新建一个项目
#python manage.py startapp appName，要在项目目录下新建模块

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('polls.urls')),
]
#何时使用 include(),当包括其它 URL 模式时你应该总是使用 include() ， admin.site.urls 是唯一例外。
#通过前面的'admin'或者'movie'，进入一个界面，除非是admin.site.urls，其他都应该用include来引导

