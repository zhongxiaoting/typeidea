"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/11 20:42
    @Author  : zhongxiaoting
    @Site    : 
    @File    : base_admin.py
    @Software: PyCharm
"""
from django.contrib import admin


class BaseOwnerAdmin(object):
    """
    1. 用来自动补充文章、分类、标签、侧边栏、友链这些Model的owner字段
    2. 用来针对 queryset 过滤当前用户的数据
    """

    # exclude = ('owner',)
    # 自动获取当前用户
    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()

    # 显示作者创建的文章
    def get_list_queryset(self):
        request = self.request
        qs = super().get_list_queryset()
        # print(qs)
        # print(request.user.is_superuser)
        if request.user.is_superuser:  # 超级用户可查看所有数据
            return qs
        return qs.filter(owner=request.user)

