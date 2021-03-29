"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/11 20:26
    @Author  : zhongxiaoting
    @Site    : 
    @File    : custom_site.py
    @Software: PyCharm
"""
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_title = "Typeidea后台管理"
    site_header = "Typeidea"
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
