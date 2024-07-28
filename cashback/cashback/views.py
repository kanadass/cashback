from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_page'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},]

data_db = [
    {'id': 1, 'title': 'qqqq', 'content': 'wwww', 'is_published': True},
    {'id': 2, 'title': 'eeee', 'content': 'rrrr', 'is_published': False},
    {'id': 3, 'title': 'ttt', 'content': 'yyy', 'is_published': True},
]

def index(request):
    template = 'cashback/index.html'
    data = {
        'title': "Site's home page",
        'menu': menu,
        'posts': data_db,
    }
    return render(request, template, context=data)


def about(request):
    template = 'cashback/about.html'
    data = {'title': "About site"}
    return render(request, template, context=data)


def show_post(request, post_id):
    return HttpResponse(f'Displaying an article with an id: {post_id}')

def addpage(request):
    return HttpResponse('Add article')


def contact(request):
    return HttpResponse('Contact form')


def login(request):
    return HttpResponse('Sign in form')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')