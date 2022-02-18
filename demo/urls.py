# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: urls.py
@time: 2022/2/17 23:20
@usage: 
"""

from django.urls import path
from demo import views

urlpatterns = [
    path('tpl', views.tpl),

]

if __name__ == '__main__':
    print('Hello world')
