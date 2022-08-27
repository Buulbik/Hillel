from django.shortcuts import render
from django.urls import reverse

from apps.blog.models import BlogCategory, Article, Tag
from config.settings import PAGE_NAMES


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current': PAGE_NAMES['blog']}
    return render(request, 'blog/category/list.html', {'categories': blog_categories, 'breadcrumbs': breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog']}
    category = BlogCategory.objects.get(id=category_id)
    if category:
        breadcrumbs.update({'current': category})
    return render(request, 'blog/article/list.html', {'articles': articles, 'breadcrumbs': breadcrumbs})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog']}
    article_name = Article.objects.get(id=article_id)
    category_name = BlogCategory.objects.get(id=category_id)
    if article_name:
        breadcrumbs.update({reverse('article_list', args=[category_id]): category_name})
    breadcrumbs.update({'current': article_name})
    return render(request, 'blog/article/view.html',
                  {'article': article, 'category': category, 'breadcrumbs': breadcrumbs})


def tag_view(request, tag_id):
    articles = Article.objects.filter(tags__in=[tag_id])
    tag = Tag.objects.get(id=tag_id)
    breadcrumbs = {'current': tag}
    return render(request, 'blog/tag/list.html', {'articles': articles, 'breadcrumbs': breadcrumbs})

