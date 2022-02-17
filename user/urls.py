# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: urls.py
@time: 2022/2/17 23:20
@usage: 
"""

from django.urls import path
from user import views

urlpatterns = [
    path('', views.index),
]

if __name__ == '__main__':
    print('Hello world')
