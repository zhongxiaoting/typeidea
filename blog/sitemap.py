"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/15 20:26
    @Author  : zhongxiaoting
    @Site    : 
    @File    : sitemap.py
    @Software: PyCharm
"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = "always"
    priority = 1
    protocol = 'https'

    def item(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def lastmod(self, obj):
        return obj.created_time

    def location(self, obj):
        return reversed('post-detail', args=[obj.pk])