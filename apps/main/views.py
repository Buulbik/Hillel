from django.shortcuts import render

from apps.main.mixins import DetailViewBreadcrumbsMixin
from apps.main.models import Page


class PageView(DetailViewBreadcrumbsMixin):
    model = Page
    template_name = 'main/page.html'

    def get_queryset(self):
        queryset = Page.objects.filter(is_active=True)
        return queryset

    def set_breadcrumbs(self):
        breadcrumbs = {'current': self.object.name}
        return breadcrumbs
