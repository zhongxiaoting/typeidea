from datetime import date

from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
from blog.models import Tag, Post, Category
from django.shortcuts import get_object_or_404

from comment.forms import CommentForm
from comment.models import Comment
from config.models import SideBar
from django.views.generic import DetailView, ListView
from django.db.models import Q, F


# def post_list(request, tag_id=None, category_id=None):
#     tag = None
#     category = None
#     # 获取文章的标题和内容
#     if tag_id:
#         post_list, tag = Post.get_by_tag(tag_id)
#     elif category_id:
#         post_list, category = Post.get_by_category(category_id)
#     else:
#         post_list = Post.latest_posts()
#     # 侧边栏
#     sidebars = SideBar.get_all()
#     context = {'category': category, 'tag': tag, 'post_list': post_list, 'sidebars': sidebars}
#     context.update(Category.get_navs())
#     return render(request, 'blog/list.html', context)

# 通用数据，比如导航、侧边栏、底部导航栏等信息
class CommentViewMixin:
    def get_context_data(self, **kwargs):
        context = super(CommentViewMixin, self).get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all()
        })
        context.update(Category.get_navs())
        return context


# 以类形式获取文章列表
class IndexView(CommentViewMixin, ListView):
    queryset = Post.latest_posts()
    paginate_by = 2
    context_object_name = 'post_list'  # 如果不设置此项，在模板中的需要使用object_list变量
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        """根据分类过滤"""
        queryset = super(CategoryView, self).queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        """根据标签过滤"""
        queryset = super(TagView, self).get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag_id=tag_id)


"""获取文章的详情"""


# 以类的形似获取文章详情
class PostDetailView(CommentViewMixin, DetailView):
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        """对用户数量进行统计和文章的访问量进行统计"""
        response = super().get(request, *args, **kwargs)
        self.handle_visited()
        return response

    def handle_visited(self):
        increase_pv = False
        increase_uv = False
        # 拿到服务端的uid
        uid = self.request.uid
        # 设置pv_key和uv_key
        pv_key = 'pv: %s: %s' % (uid, self.request.path)
        uv_key = 'uv: %s: %s: %s' % (uid, str(date.today()), self.request.path)
        # 对服务端的缓存信息用户pv_key进行判断
        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key, 1, 1 * 60)  # 1分钟有效
        if not cache.get(uv_key):
            increase_uv = True
            cache.set(uv_key, 1, 60 * 60 * 24)  # 1天有效
        # 如果用户还没访问过文章，将文章的统计量进行+1
        if increase_pv and increase_uv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1, uv=F('uv') + 1)
        elif increase_pv:
            Post.objects.filter(pk=self.request.id).update(pv=F('pv') + 1)
        elif increase_uv:
            Post.objects.filter(pk=self.object.id).update(uv=F('uv') + 1)


# def post_detail(request, post_id=None):
# try:
#     post = Post.objects.get(id=post_id)
# except Post.DoesNotExist:
#     post = None
# context = {
#     'post': post,
# }
# context.update(Category.get_navs())
# return render(request, 'blog/detail.html', context)


class SearchView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data()
        context.update({
            'keyword': self.request.GET.get('keyword')
        })
        return context

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))


class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.kwargs.get('owner_id')  # TODO
        print(owner_id)
        return queryset.filter(owner_id=owner_id)
