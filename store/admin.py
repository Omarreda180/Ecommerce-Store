from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created', 'updated', 'is_available']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['is_available', 'category']
    list_editable = ['price', 'is_available', 'stock']
    readonly_fields = ['created', 'updated', ]