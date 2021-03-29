"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/15 17:23
    @Author  : zhongxiaoting
    @Site    : 
    @File    : rss.py
    @Software: PyCharm
"""
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed

from blog.models import Post


class ExtendedRSSFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed, self).add_item_elements(handler, item)
        handler.addQuickElement('content:html', item['content_html'])


class LatestPostFeed(Feed):    #TODO
    feed_type = Rss201rev2Feed
    title = 'Typeidea Blog System'
    link = '/rss/'
    description = "typeidea is a blog system power by django"

    def item(self):
        print(Post.objects.filter(status=Post.STATUS_NORMAL)[:2])
        return Post.objects.filter(status=Post.STATUS_NORMAL)[:2]

    def item_title(self, item):
        return self.title

    def item_description(self, item):
        return self.description

    def item_link(self, item):
        return reversed('post-detail', args=[item.pk])

    def item_extra_kwargs(self, item):
        return {'content_html': self.item_content_html(item)}

    def item_content_html(self, item):
        return item.content_html
