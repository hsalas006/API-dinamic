from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    filedsets = (
        (None, {'fiels': ('email', 'password')}),
        (('Person Info'), {'fields': ('name',)}),
        (
            ('Permissions'),
            {'fields':('is_active', 'is_staff', 'is_superuser')}
        ),
        (('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(models.User, UserAdmin)
