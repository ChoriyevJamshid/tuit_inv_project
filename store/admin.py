from django.contrib import admin

from django.apps import apps
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['title', 'slug', 'price',
                    'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'updated_at']
    list_editable = ['price', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
