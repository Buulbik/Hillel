from django.db import models
from tinymce.models import HTMLField

from apps.main.mixins import MetaTagMixin


class Page(MetaTagMixin):
    name = models.CharField(verbose_name='Название', max_length=128)
    slug = models.SlugField(unique=True)
    text = HTMLField(verbose_name='Описание', null=True)
    is_active = models.BooleanField(verbose_name='Активировано', default=True)

    class Meta:
        verbose_name = 'Информационная страница'
        verbose_name_plural = 'Информационные страницы'

    def __str__(self):
        return self.name

