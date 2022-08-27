from django.urls import reverse

from apps.catalog.models import Category, Product
from apps.main.mixins import DetailViewBreadcrumbsMixin, ListViewBreadcrumbsMixin
from config.settings import PAGE_NAMES


class CatalogIndexView(ListViewBreadcrumbsMixin):
    model = Category
    template_name = 'catalog/index.html'

    def set_breadcrumbs(self):
        breadcrumbs = {'current': PAGE_NAMES['catalog']}
        return breadcrumbs

    def get_queryset(self):
        return Category.objects.filter(parent=None)


class ProductByCategoryView(ListViewBreadcrumbsMixin):
    template_name = 'catalog/category.html'
    category = None
    categories = Category.objects.all()

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(categories=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductByCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = self.categories
        return context

    def set_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog']}
        if self.category.parent:
            links = []
            parent = self.category.parent
            while parent is not None:
                links.append((reverse('category', args=[parent.slug]), parent.name))
                parent = parent.parent
            for url, name in links[::-1]:
                breadcrumbs.update({url: name})
        breadcrumbs.update({'current': self.category.name})
        return breadcrumbs


class ProductDetailView(DetailViewBreadcrumbsMixin):
    model = Product
    template_name = 'catalog/product.html'

    def set_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog']}
        category = self.object.main_category()
        if category:
            breadcrumbs.update({reverse('category', args=[category.slug]): category.name})
        breadcrumbs.update({'current': self.object.name})
        return breadcrumbs
