import mistune
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# 分类表
from django.utils.functional import cached_property


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    # 分类名
    name = models.CharField(max_length=50, verbose_name='名称')
    # 状态
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    # 是否为导航
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    # 作者
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    # 日期
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'
        db_table = 'Category'

    # 对blog/views.py数据进行操作
    @classmethod
    def get_navs(cls):
        categories = cls.objects.filter(status=cls.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)
        return {
            'nav': nav_categories,
            'categories': normal_categories,
        }


# 标签表
class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    # 名称
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'  # 复数和单数都是’标签‘这个名字


# 文章内容表
class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿')
    )
    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.TextField(verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文必须为MarkDown格式')
    content_html = models.TextField(verbose_name='正文html代码', blank=True, editable=False) # 不需要人为编辑
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    pv = models.PositiveIntegerField(default=1)  # 统计文章数
    uv = models.PositiveIntegerField(default=1)  # 统计浏览数

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']  # 根据id进行降序排列

    # 对blog/views.py进行处理
    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        post_list = tag.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        post_list = category.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        return category, post_list

    @classmethod
    def latest_posts(cls):
        queryset = cls.objects.filter(status=cls.STATUS_NORMAL)
        return queryset

    @classmethod
    def hot_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-pv')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.content_html = mistune.markdown(self.content)
        super(Post, self).save()

    @cached_property
    def tags(self):
        return ','.join(self.tag.values_list('name', flat=True))
