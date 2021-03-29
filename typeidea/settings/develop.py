"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/8 10:17
    @Author  : zhongxiaoting
    @Site    : 
    @File    : develop.py
    @Software: PyCharm
"""
from .base import *  # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_blog',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'zhongxiaoting'
    }
}