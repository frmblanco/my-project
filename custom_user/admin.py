from django.contrib import admin
from custom_user.models import CustomUser
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('email', 'username', 'first_name', 'last_name', )}),
    )

admin.site.register(CustomUser, MyUserAdmin)

