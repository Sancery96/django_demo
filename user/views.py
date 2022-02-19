from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from user.models import UserInfo


def index(request):
    return HttpResponse('用户首页')


def user_list(request):
    # setting下的Template-Dirs为[]时，根据app的注册顺序，到每个app的templates目录下寻找
    # setting下的Template-Dirs为[BASE_DIR / 'templates']时，先到根目录的templates寻找，
    # 如果未找到，再根据app的注册顺序，到每个app的templates目录下寻找
    users = UserInfo.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        password = request.POST.get('password')
        UserInfo.objects.create(name=name, age=age, password=password)
        return redirect('./lists')
    return render(request, 'user_add.html')


def user_edit(request):
    return render(request, 'user_edit.html')


def user_del(request, name):
    UserInfo.objects.filter(name=name).delete()
    return redirect('../lists')
    # return HttpResponse('删除用户')
