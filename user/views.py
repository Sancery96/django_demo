from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('用户首页')


def user_list(request):
    # setting下的Template-Dirs为[]时，根据app的注册顺序，到每个app的templates目录下寻找
    # setting下的Template-Dirs为[BASE_DIR / 'templates']时，先到根目录的templates寻找，
    # 如果未找到，再根据app的注册顺序，到每个app的templates目录下寻找
    return render(request, 'user_list.html')


def user_add(request):
    return render(request, 'user_add.html')


def user_edit(request):
    return render(request, 'user_edit.html')


def user_del(request):
    return HttpResponse('删除用户')
