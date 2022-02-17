from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('用户首页')


def user_list(request):
    return HttpResponse('用户列表')


def user_add(request):
    return HttpResponse('添加用户')


def user_edit(request):
    return HttpResponse('编辑用户')


def user_del(request):
    return HttpResponse('删除用户')

