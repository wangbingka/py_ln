#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/23  23:16
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from django.urls import path

from . import views

urlpatterns = [
    path('123', views.index, name='index'),
]