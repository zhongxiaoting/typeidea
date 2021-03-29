"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/14 16:16
    @Author  : zhongxiaoting
    @Site    : 
    @File    : urls.py
    @Software: PyCharm
"""
from django.urls import path

from comment.views import CommentView

app_name = 'comment'
urlpatterns = [
    path('comment-list/', CommentView.as_view(), name='comment'),
]