from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


menu = ['About site', ' Add article', 'Feedback', 'Sign in']

data_db = [
    {'id': 1, 'title': 'qqqq', 'content': 'wwww', 'is_published': True},
    {'id': 2, 'title': 'eeee', 'content': 'rrrr', 'is_published': False},
    {'id': 333, 'title': 'ttt', 'content': 'yyy', 'is_published': True},
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


def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories page</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Categories page by slug</h1><p>slug: {cat_slug}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')