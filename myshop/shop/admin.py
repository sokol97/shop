from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updates', 'category', 'image']
    list_filter = ['available', 'created', 'updates']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
