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


def tpl(request):
    name = '忍冬'
    seasons = ['春', '夏', '秋', '冬']
    herb = {'name': '桔梗', 'function': '生津止咳', 'img': '../static/img/Kikyo.jpeg'}
    herbs = [{'name': '桔梗', 'function': '生津止咳', 'img': '../static/img/Kikyo.jpeg'},
             {'name': '当归', 'function': '补血活血，调经止痛，润肠通便', 'img': '../static/img/Danggui.jpeg'}]

    return render(request, 'tpl.html', {'n1': name, 'n2': seasons, 'n3': herb, 'n4': herbs})
