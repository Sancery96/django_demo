from django.shortcuts import render, redirect


# Create your views here.


def tpl(request):
    name = '忍冬'
    seasons = ['春', '夏', '秋', '冬']
    herb = {'name': '桔梗', 'function': '生津止咳', 'img': '../static/img/Kikyo.jpeg'}
    herbs = [{'name': '桔梗', 'function': '生津止咳', 'img': '../static/img/Kikyo.jpeg'},
             {'name': '当归', 'function': '补血活血，调经止痛，润肠通便', 'img': '../static/img/Danggui.jpeg'}]

    return render(request, 'tpl.html', {'n1': name, 'n2': seasons, 'n3': herb, 'n4': herbs})


def books(request):
    import requests
    from bs4 import BeautifulSoup
    url = 'https://book.douban.com/top250?icn=index-book250-all'
    headers = {
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }

    html = requests.get(url, headers=headers)
    # print(html.text)
    soup = BeautifulSoup(html.text)
    books = soup.select('.item')
    book_list = []
    for book in books:
        info = {
            'title': book.select_one('.pl2').a.get_text(),
            'link': book.select_one('.pl2').a.get('href'),
            'author': book.select_one('p.pl').text,
            'score': book.select_one('.rating_nums').text,
            'quote': book.select_one('.inq').text,
            'img': book.select_one('img')['src']
        }
        book_list.append(info)
    # print(books)

    return render(request, 'books.html', {'books': book_list})


def login(request):
    if request.method == 'POST':
        e_mail = request.POST.get('email')
        password = request.POST.get('pswd')
        print(e_mail, password)
        if e_mail == 'root@qq.com' and password == '123456':
            return redirect('./books')
        else:
            return render(request, 'login_v1.html', {'error_msg': '用户名或密码错误'})
    return render(request, 'login_v1.html')
