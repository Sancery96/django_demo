# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: user.py
@time: 2022/2/19 20:40
@usage: 
"""
from django.shortcuts import render, redirect

from staff_manage_system.models.depart import Depart
from staff_manage_system.models.user import User


def user_list(request):
    users = User.objects.all()
    return render(request, 'ulist.html', {'users': users})


def user_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        depart_title = request.POST.get('depart')
        depart = Depart.objects.filter(title=depart_title).first()
        User.objects.create(name=name, age=age, password=password, gender=gender, depart=depart)
        return redirect('ulists')
    return render(request, 'uedit.html', {'page_title': '添加员工'})


def user_edit(request, uid):
    user = User.objects.filter(id=uid)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        depart_title = request.POST.get('depart')
        depart = Depart.objects.filter(title=depart_title).first()
        user.update(name=name, age=age, password=password, gender=gender, depart=depart)
        return redirect('ulists')
    return render(request, 'uedit.html', {'user': user.first(), 'page_title': '编辑员工'})


def user_del(request):
    uid = request.GET.get('uid')
    User.objects.filter(id=uid).delete()
    return redirect('ulists')


if __name__ == '__main__':
    print('Hello world')
