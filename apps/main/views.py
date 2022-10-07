from apps.main.mixins import DetailViewBreadcrumbsMixin
from apps.main.models import Page, ProductSet
from django.shortcuts import render


def home(request):
    product_sets = ProductSet.objects.filter(is_active=True)
    return render(request, 'index.html', {'product_sets': product_sets})


class PageView(DetailViewBreadcrumbsMixin):
    model = Page
    template_name = 'main/page.html'

    def get_queryset(self):
        queryset = Page.objects.filter(is_active=True)
        return queryset

    def set_breadcrumbs(self):
        breadcrumbs = {'current': self.object.name}
        return breadcrumbs
