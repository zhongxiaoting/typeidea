from django.shortcuts import render

# Create your views here.
from blog.views import CommentViewMixin
from .models import Link
from django.views.generic import ListView


# 怎加友链页面
class LinkListView(CommentViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'
