from django.urls import path
from .views import index, blog, post, search

urlpatterns = [
    path('blogs/', blog, name = 'blog'),
    path('posts/<slug>/', post, name = 'post'),
    path('', index, name = 'index'),
    path('search/' , search, name = 'search')
    ]