from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('用户首页')


def user_list(request):
    return render(request, 'user_list.html')


def user_add(request):
    return render(request, 'user_add.html')


def user_edit(request):
    return render(request, 'user_edit.html')


def user_del(request):
    return HttpResponse('删除用户')

