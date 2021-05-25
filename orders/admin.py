from django.contrib import admin
from .models import Payment, Order, OrderProduct
from django.utils.html import format_html


class OrderProdcutInline(admin.TabularInline):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="75" height="110">'.format(object.product.image.url))
    thumbnail.short_description = 'Product Picture'
    model = OrderProduct
    readonly_fields = ['thumbnail','product','variations','product_price', 'quantity','user','payment',    'ordered',  ]
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'email', 'phone', 'order_total', 'status', 'is_ordered' ]
    list_filter = ['is_ordered', 'status']
    list_per_page = 20
    inlines = [OrderProdcutInline]
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'product_price', 'ordered']
    list_filter = ['ordered', 'product']
    list_per_page = 20

admin.site.register(Payment)


# 
# 
# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     def thumbnail(self, object):
#         return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
#     thumbnail.short_description = 'Profile Picture'
#     list_display = ('thumbnail', 'user', 'city', 'state', 'country')
# 