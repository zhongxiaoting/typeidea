"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/15 14:54
    @Author  : zhongxiaoting
    @Site    : 
    @File    : user_id.py
    @Software: PyCharm
"""
import uuid

USER_KEY = 'uid'
THE_YEARS = 60 * 60 * 24 * 365 * 10


class UserIDMiddleware:
    """对用户的访问数量进行统计，确定每一个用户只能访问一次"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 获取uid
        uid = self.generate_uid(request)
        # 将uid赋给request
        request.uid = uid
        # 返回response，设置COOKIE，并设置只有服务端可以访问
        response = self.get_response(request)
        response.set_cookie(USER_KEY, max_age=THE_YEARS, httponly=True)
        return response

    def generate_uid(self, request):
        try:  # TODO
            # uid = request.COOKIES[USER_KEY]
            uid = uuid.uuid4().hex
            request.COOKIES[USER_KEY] = uid
            # print(request.COOKIES)
        except KeyError:
            uid = uuid.uuid4().hex
        return uid
