from django.contrib import admin
from apps.blog.models import Article, BlogCategory

# from apps.blog.models import Tag


admin.site.register(Article)
admin.site.register(BlogCategory)

