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
    path('lists', views.user_list),
    path('add', views.user_add),
    path('edit', views.user_edit),
    path('del', views.user_del),

]

if __name__ == '__main__':
    print('Hello world')
