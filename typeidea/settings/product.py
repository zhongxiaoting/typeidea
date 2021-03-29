"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/23 20:36
    @Author  : zhongxiaoting
    @Site    : 
    @File    : product.py
    @Software: PyCharm
"""
from django.conf.global_settings import MANAGERS

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'

EMAIL_PORT = 25 #SMTP端口
EMAIL_HOST_USER = 'z1915270314@163.com' #发送邮件的邮箱
EMAIL_HOST_PASSWORD = '******'  # 授权码
EMAIL_SUBJECT_PREFIX = '[一念永恒的博客] ' #为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = False  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)默认false
DEFAULT_FROM_EMAIL = 'z1915270314@163.com'
