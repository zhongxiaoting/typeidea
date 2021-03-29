"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/12 21:23
    @Author  : zhongxiaoting
    @Site    : 
    @File    : urls.py
    @Software: PyCharm
"""
from django.urls import path

from config.views import LinkListView
app_name = 'config'
urlpatterns = [
    path('link/', LinkListView.as_view(), name='links')
]