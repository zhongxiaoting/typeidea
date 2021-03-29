from django.contrib import admin

# Register your models here.
from django.contrib.admin.models import LogEntry

import xadmin
from blog.models import Category, Tag, Post
from django.urls import reverse
from django.utils.html import format_html
from common.base_admin import BaseOwnerAdmin
from xadmin.filters import manager
from xadmin.layout import Fieldset, Row
from xadmin.filters import RelatedFieldListFilter


class CategoryOwnerFilter(RelatedFieldListFilter):
    """自定义过滤器只展示当前用户分类"""
    title = "作者创建的‘分类’"
    parameter_name = "owner_category"

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        # 重新获取lookup_choices，根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


class CategoryAdmin(BaseOwnerAdmin):
    # 计算文章总数
    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')


xadmin.site.register(Category, CategoryAdmin)


class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


xadmin.site.register(Tag, TagAdmin)


class PostAdmin(BaseOwnerAdmin):
    def post_tag(self, obj):
        p_tag = []
        for pt in obj.tag.all():
            p_tag.append(pt.name)
        # print(p_tag)
        return ','.join(p_tag)

    post_tag.short_description = '标签'
    #
    # exclude = ('owner',)
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag'
    # )
    form_layout = (
        Fieldset(
            '基础信息',
            Row('title', 'category', 'status', 'tag')
        ),
        Fieldset(
            '内容信息',
            'des', 'content',
        )
    )
    list_display = ['title', 'category', 'post_tag', 'status', 'created_time', 'owner', 'operator']
    list_display_links = []
    list_filter = ['category']
    search_fields = ['title', 'category__name']
    actions_on_top = True
    # actions_on_bottom = True

    # 编辑页面
    fields = (
        'category',
        'title',
        'desc',
        'status',
        'content',
        'tag'
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            self.model_admin_url('change', obj.id)
        )

    operator.short_description = '操作'


xadmin.site.register(Post, PostAdmin)
