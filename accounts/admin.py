from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display =[
        "email",
        "username",
        "name",
        "is_staff"
    ]

fieldsets = UserAdmin.fieldsets +((None, {'fields':('name',)}),)
add_fieldsets = UserAdmin.add_fieldsets +((None, {'fields':('name',)}),)

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
