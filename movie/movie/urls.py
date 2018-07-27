#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/23  23:16
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from django.urls import path

from . import views

#http://127.0.0.1:8000/movie/subject/%E6%95%99%E7%88%B6/

urlpatterns = [
    path('subject/<str:name>/', views.index),
    path('add/', views.add),  #通过add/，触发add方法，后面不能加()
]

#urlpatterns常见写法
""" u
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    
"""

#http://127.0.0.1:8000/movie/subject/字符串形式的文字,需要输入这个提示，进入下一层
#'subject/<str:name>/'在网页输入时，后面也需要有“/”，'subject/<str:name>'这里没有，网址里也不能有