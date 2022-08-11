from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField
from mptt.models import MPTTModel, TreeForeignKey
from pilkit.processors import ResizeToFill
from django.urls import reverse
from config.settings import MEDIA_ROOT


class Category(MPTTModel):
    name = models.CharField(verbose_name='Название', max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    parent = TreeForeignKey(
        to='self',
        related_name='child',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description = 'Текущее изображение'
    image_tag_thumbnail.allow_tags = True

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Текущее изображение'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        full_path = [self.name]
        parent = self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        return ' -> '.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

