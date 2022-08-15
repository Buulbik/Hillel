from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
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


class Image(models.Model):
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='catalog/',
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

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description = 'Текущее изображение товара'
    image_tag_thumbnail.allow_tags = True

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Текущее изображение товара'
    image_tag.allow_tags = True


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    categories = models.ManyToManyField(
        to=Category,
        verbose_name='Категории',
        through='ProductCategory',
        related_name='categories',
        blank=True
    )
    images = models.ManyToManyField(
        to=Image,
        verbose_name='Категории',
        trough='ProductImage',
        related_name='images',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, verbose_name='Категория', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основная категория', default=False)

    def __str__(self):
        return ''

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_main:
            ProductCategory.objects.filter(product=self.product).update(is_main=False)
        super(ProductCategory, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'


class ProductImage(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    image = models.ForeignKey(to=Image, verbose_name='Изображение', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основное изображение', default=False)

    def __str__(self):
        return ''

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_main:
            ProductImage.objects.filter(product=self.product).update(is_main=False)
        super(ProductImage, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'
