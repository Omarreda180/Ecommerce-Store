from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['email','last_login' , 'username', 'is_active']
    readonly_fields = ['date_joined', 'last_login', ]
    ordering = ('-date_joined_for_format',)
    list_filter = ['is_active']
