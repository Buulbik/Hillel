from django.db import models
from django.views import generic


class MetaTagMixin(models.Model):
    name = None
    meta_title = models.CharField(verbose_name='Meta Title', max_length=255, null=True, blank=True)
    meta_description = models.TextField(verbose_name='Meta Description', null=True, blank=True)
    meta_keywords = models.CharField(verbose_name='Meta Keywords', max_length=255, null=True, blank=True)

    def get_meta_title(self):
        if self.meta_title:
            return self.meta_title
        return self.name

    class Meta:
        abstract = True


class ListViewBreadcrumbsMixin(generic.ListView):
    breadcrumbs = {}

    def set_breadcrumbs(self):
        return self.breadcrumbs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.set_breadcrumbs()
        return context


class DetailViewBreadcrumbsMixin(generic.DetailView):
    breadcrumbs = {}

    def set_breadcrumbs(self):
        return self.breadcrumbs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.set_breadcrumbs()
        return context
