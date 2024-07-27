from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse('Cashback page')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories page</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Categories page by slug</h1><p>slug: {cat_slug}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')