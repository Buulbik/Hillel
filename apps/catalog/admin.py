from django.contrib import admin
from apps.catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity', 'price']
    list_display_links = ['id', 'name']
    fields = ['name', 'description',  'quantity', 'price']
