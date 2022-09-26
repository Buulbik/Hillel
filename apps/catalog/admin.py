from django.contrib import admin
from apps.catalog.models import Category, Product, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    fields = ['name', 'slug', 'parent', 'description', 'image_tag', 'image',
              'meta_title', 'meta_description', 'meta_keywords']
    readonly_fields = ['image_tag']


class ProductCategoryInline(admin.TabularInline):
    model = Product.categories.through
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['product', 'image_tag', 'image', 'is_main']
    readonly_fields = ['image_tag']
    extra = 1


@admin.register(Product)
class Product(admin.ModelAdmin):
    fields = ['name', 'description', 'quantity', 'price', 'is_checked', 'user', 'meta_title', 'meta_description',
              'meta_keywords']
    list_display = ['id', 'name', 'user', 'quantity', 'price', 'is_checked']
    list_display_links = ['id', 'name']
    inlines = [ProductCategoryInline, ImageInline]






