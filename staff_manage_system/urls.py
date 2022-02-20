# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: urls.py
@time: 2022/2/19 20:18
@usage: 
"""

from django.urls import path
from staff_manage_system.views import user, depart

urlpatterns = [
    # path('', views.index),
    # 部门管理
    path('dlists/', depart.depart_list, name='dlists'),
    path('dadd', depart.depart_add, name='dadd'),
    path('dedit/<str:dpid>', depart.depart_edit, name='dedit'),
    path('ddel/', depart.depart_del, name='ddel'),

    # 员工管理
    path('ulists/', user.user_list, name='ulists'),
    path('uadd/', user.user_add, name='uadd'),
    path('uedit/<str:uid>', user.user_edit, name='uedit'),
    path('udel/', user.user_del, name='udel'),

]
if __name__ == '__main__':
    print('Hello world')
