from django.contrib import admin
from .forms import CustomUserCreationForm, SignUpForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = SignUpForm
    list_display = ('email', 'username', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)
