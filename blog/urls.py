"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/12 10:16
    @Author  : zhongxiaoting
    @Site    : 
    @File    : urls.py
    @Software: PyCharm
"""

from django.conf.urls import url
from django.urls import path, include


from blog import views
from blog.apis import PostViewSet
from blog.rss import LatestPostFeed
from blog.views import IndexView, PostDetailView, CategoryView, TagView, SearchView, AuthorView
from common.autocomplete import CategoryAutocomplete, TagAutocomplete
app_name= 'blog'

urlpatterns = [
    path('post-list/', IndexView.as_view(), name='post-list'),
    # path('api/post/', post_list, name='post-list'),
    # path('api/post/', PostViewSet.as_view(), name='post-list'),

    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category-list'),
    path('tag/<int:pk>/', TagView.as_view(), name='tag-list'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<int:pk>/', AuthorView.as_view(), name='author'),
    path('rss/', LatestPostFeed(), name='rss'),
    path('category-authcomplete/', CategoryAutocomplete.as_view(), name='categry-authcomplete'),
    path('tag-authcomplete/', TagAutocomplete.as_view(), name='tag-authcomplete'),




]