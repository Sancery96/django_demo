import datetime

from django.db import models

# Create your models here.


class Depart(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name='部门名称', max_length=32)
    created_time = models.DateTimeField(verbose_name="成立时间", default=datetime.datetime.now)

