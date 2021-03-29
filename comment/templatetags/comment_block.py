"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/14 16:54
    @Author  : zhongxiaoting
    @Site    : 
    @File    : comment_block.py
    @Software: PyCharm
"""

from django import template

from comment.forms import CommentForm
from comment.models import Comment

register = template.Library()

@register.inclusion_tag('comment/block.html')

def comment_block(target):
    return {
        'target': target,
        'comment_form': CommentForm(),
        'comment_list': Comment.get_by_target(target),
    }