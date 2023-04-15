from django.contrib import admin
from .models import Channel_Integration, Carrier_Integration, Order, Account
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email','mobile_no','is_staff','is_active')
    list_filter = ('is_staff','is_active')
    fieldsets = (
        (None, {'fields': ('first_name','last_name','email','mobile_no','password')}),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        }),
        ('Permissions', {'fields': ('is_staff','is_active','is_superuser')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields': ('first_name','last_name','email','mobile_no','password1','password2','is_staff','is_active','is_superuser')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser,CustomUserAdmin)

admin.site.register(Channel_Integration)

admin.site.register(Carrier_Integration)

admin.site.register(Order)

admin.site.register(Account)