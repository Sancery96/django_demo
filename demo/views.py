from django.shortcuts import render

# Create your views here.


def tpl(request):
    name = '忍冬'
    seasons = ['春', '夏', '秋', '冬']
    herb = {'name': '桔梗', 'function': '生津止咳', 'img': '../static/img/Kikyo.jpeg'}
    herbs = [{'name': '桔梗', 'function': '生津止咳', 'img': '../static/img/Kikyo.jpeg'},
             {'name': '当归', 'function': '补血活血，调经止痛，润肠通便', 'img': '../static/img/Danggui.jpeg'}]

    return render(request, 'tpl.html', {'n1': name, 'n2': seasons, 'n3': herb, 'n4': herbs})
