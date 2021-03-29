"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/21 21:12
    @Author  : zhongxiaoting
    @Site    : 
    @File    : serializers.py
    @Software: PyCharm
"""
from rest_framework import serializers

from config.models import SideBar


class SideBarSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = SideBar
        fields = ('id', 'title', 'status', 'content', 'owner', 'created_time')

