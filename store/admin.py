from django.contrib import admin
from .models import Category, Product, Variation, ReviewRating

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

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value', 'is_active']
    list_filter = ['product', 'variation_category', 'is_active']
    list_editable = ['is_active']

admin.site.register(ReviewRating)