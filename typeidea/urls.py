"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.apis import PostViewSet, CategoryViewSet
from blog.sitemap import PostSitemap
from blog.views import  IndexView
from django.contrib.sitemaps.views import sitemap

import xadmin
from config.apis import SideBarViewSet

xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api-post')
router.register(r'category', CategoryViewSet, basename='api-category')
router.register(r'sidebar', SideBarViewSet, basename='api-sidebar')
xversion.register_models()
urlpatterns = [
    path('admin/', xadmin.site.urls, name='xadmin'),
    # path('admin/', custom_site.urls)
    path('blog/', include('blog.urls', namespace='blog')),
    path('config/', include('config.urls', namespace='config')),
    path('comment/', include('comment.urls', namespace='comment')),
    # url(r'^$', views.post_list)
    url(r'^$', IndexView.as_view()),

    path('templates/sitemap/', sitemap, {'sitemaps': {'posts': PostSitemap}},
    name='django.contrib.sitemaps.views.sitemap'),
    path('api/', include(router.urls)),

]
