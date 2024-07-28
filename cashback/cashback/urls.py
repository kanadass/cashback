from django.urls import path

from cashback.views import index, categories, categories_by_slug, about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cats/<int:cat_id>/', categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', categories_by_slug, name='cats'),
]