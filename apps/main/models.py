from django.contrib.admin import display
from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField

from apps.catalog.models import Product
from apps.main.mixins import MetaTagMixin
from config.settings import MEDIA_ROOT


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


class ProductSet(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)
    products = models.ManyToManyField(Product, verbose_name='Товары')
    sort = models.PositiveIntegerField(default=0, blank=False, null=False)
    is_active = models.BooleanField(verbose_name='Активировано', default=True)

    class Meta:
        ordering = ['sort']
        verbose_name = 'Карусель товаров'
        verbose_name_plural = 'Карусели товаров'

    def __str__(self):
        return self.name


class GlobalSetting(MetaTagMixin):
    main_text = HTMLField(verbose_name='Текст на главной')
    footer_text = models.CharField(verbose_name='Текст в футере', max_length=255)
    logo = models.ImageField(verbose_name='Изображение', upload_to='main', null=True)

    @display(description='Текущий логотип')
    def image_tag_thumbnail(self):
        if self.logo:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.logo}' width='70'>")

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

    def __str__(self):
        return 'Настройки'

