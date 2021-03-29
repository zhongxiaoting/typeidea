"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/23 21:11
    @Author  : zhongxiaoting
    @Site    : 
    @File    : send_email.py
    @Software: PyCharm
"""
from typeidea.settings import product
from django.core.mail import send_mail


def send(request):
    """发送邮件"""
    subject = "看看我的博客吧"
    message = "我的博客里面有很多好看的文章！"
    sender = product.DEFAULT_FROM_EMAIL  # 发送邮箱
    receiver = ['1915270314@qq.com']  # 接收邮箱
    send_mail(subject, message, sender, receiver)


send()
