import admin_thumbnails

from django.contrib import admin
from .models import Category, Product, Variation, ReviewRating, ProductGallery


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

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
    inlines = [ProductGalleryInline]

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value', 'is_active']
    list_filter = ['product', 'variation_category', 'is_active']
    list_editable = ['is_active']

@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_filter = ['product']

admin.site.register(ReviewRating)
