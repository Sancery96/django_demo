# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: user.py
@time: 2022/2/19 20:22
@usage: 
"""
import datetime

from django.db import models


class User(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name='员工姓名', max_length=32)
    age = models.IntegerField(verbose_name='年龄', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    hiredate = models.DateTimeField(verbose_name='入职时间', default=datetime.datetime.now)

    # 若字段内容为固定值时，可用数字代替字符在数据库中表示，从而减少占用空间，加快检索速度
    gender_choice = (
        (0, '男'),
        (1, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choice)

    # 一对多，实际在数据库中保存的字段为：depart_id
    depart = models.ForeignKey(to="Depart", to_field='id', on_delete=models.CASCADE)


if __name__ == '__main__':
    print('Hello world')
