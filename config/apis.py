"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/21 21:36
    @Author  : zhongxiaoting
    @Site    : 
    @File    : apis.py
    @Software: PyCharm
"""
from rest_framework import viewsets

from blog.models import Post
from config.serializers import SideBarSerializer


class SideBarViewSet(viewsets.ModelViewSet):
    serializer_class = SideBarSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)