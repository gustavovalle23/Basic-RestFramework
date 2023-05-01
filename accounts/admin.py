from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import User


class UserAdmin(BaseUserAdmin):
    ordering = ("id",)
    list_display = [
        "id",
        "email",
        "username",
        "birth_date",
        "is_active",
        "date_joined",
        "is_staff",
    ]
    list_filter = [
        "is_active",
    ]


admin.site.register(User, UserAdmin)
