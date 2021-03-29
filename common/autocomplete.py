"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/19 15:51
    @Author  : zhongxiaoting
    @Site    : 
    @File    : autocomplete.py
    @Software: PyCharm
"""
from dal import autocomplete

from blog.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Category.objects.none()

        qs = Category.objects.filter(owner=self.request.user)
        # q是url参数上传递过来的值
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()
        qs = Tag.objects.filter(owner=self.request.user)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
