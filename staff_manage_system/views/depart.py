from django.shortcuts import render, redirect

# Create your views here.
from staff_manage_system.models.depart import Depart


def depart_list(request):
    departs = Depart.objects.all()
    return render(request, 'depart_list.html', {'departs': departs})


def depart_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Depart.objects.create(title=title)
        return redirect('dlists')
    return render(request, 'depart_edit.html', {'page_title': '添加部门'})


def depart_edit(request, dpid):
    depart = Depart.objects.filter(id=dpid)
    if request.method == 'POST':
        title = request.POST.get('title', depart.first().title)
        depart.update(title=title)
        return redirect('dlists')
    return render(request, 'depart_edit.html', {'depart': depart.first(), 'page_title': '编辑部门'})


def depart_del(request):
    dpid = request.GET.get('dpid')
    Depart.objects.filter(id = dpid).delete()
    return redirect('dlists')