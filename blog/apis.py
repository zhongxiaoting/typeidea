"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/21 11:29
    @Author  : zhongxiaoting
    @Site    : 
    @File    : apis.py
    @Software: PyCharm
"""
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post, Category
from blog.serializers import PostSerializer, PostDetailSerializer, CategorySerializer, CategoryDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super(PostViewSet, self).retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super(CategoryViewSet, self).retrieve(request, *args, **kwargs)
        

