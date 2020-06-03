from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms


class CustomUserCreationForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
