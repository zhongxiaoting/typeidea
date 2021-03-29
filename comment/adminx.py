# Register your models here.
import xadmin
from comment.models import Comment


class CommentAdmin(object):
    list_display = ('target', 'nickname', 'website', 'email', 'status', 'created_time')


xadmin.site.register(Comment, CommentAdmin)
