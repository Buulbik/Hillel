from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill

from apps.main.mixins import MetaTagMixin
from config.settings import MEDIA_ROOT
from apps.user.models import User
from tinymce.models import HTMLField


class BlogCategory(MetaTagMixin):
    name = models.CharField(verbose_name='Название', max_length=255)
    # image = models.ImageField(verbose_name='Изображение', upload_to='blog/category/', null=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категории блога'


class Tag(MetaTagMixin):
    name = models.CharField(verbose_name='Тэги', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Article(MetaTagMixin):
    category = models.ForeignKey(
        to=BlogCategory,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/article/',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100}
    )
    text_preview = models.TextField(verbose_name='Текст-превью')
    text = HTMLField(verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name="Тэги", blank=True)
    user = models.ForeignKey(
        to=User,
        verbose_name='Пользователь',
        on_delete=models.SET_NULL,
        null=True)

    def get_meta_title(self):
        if self.meta_title:
            return self.meta_title
        return self.title

    def image_tag_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                Article.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='70'>")

    image_tag_thumbnail.short_description = 'Текущее изображение'
    image_tag_thumbnail.allow_tags = True

    def image_tag(self):
        if self.image:
            if not self.image_thumbnail:
                Article.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}'>")

    image_tag.short_description = 'Текущее изображение'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    user = models.ForeignKey(to=User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(verbose_name='Имя', max_length=128, null=True, blank=True)
    email = models.EmailField(verbose_name='E-mail')
    article = models.ForeignKey(to=Article, verbose_name='Статья', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    is_checked = models.BooleanField(verbose_name='Проверен ли', default=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

