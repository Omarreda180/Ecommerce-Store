from django.contrib import admin
from .models import Payment, Order, OrderProduct

class OrderProdcutInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ['payment', 'user', 'product', 'quantity', 'ordered', 'product_price']
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

