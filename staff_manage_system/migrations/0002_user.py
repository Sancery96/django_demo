# Generated by Django 3.2.12 on 2022-02-20 04:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff_manage_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='员工姓名')),
                ('age', models.IntegerField(max_length=32, verbose_name='年龄')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('hiredate', models.DateTimeField(default=datetime.datetime.now, verbose_name='入职时间')),
                ('gender', models.SmallIntegerField(choices=[(0, '男'), (1, '女')], verbose_name='性别')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff_manage_system.depart')),
            ],
        ),
    ]
