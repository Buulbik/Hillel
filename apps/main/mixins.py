from django.db import models


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

