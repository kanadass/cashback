from django.urls import path

from cashback.views import index, categories, categories_by_slug

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:cat_id>/', categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', categories_by_slug, name='cats'),
]