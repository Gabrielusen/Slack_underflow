from django import forms
from .models import PostAnswer, PostQuestion
from django.db import models
# from tinymce.widgets import TinyMCE
from pagedown.widgets import AdminPagedownWidget


class PostForm(forms.ModelForm):
    text_content = forms.CharField(widget=AdminPagedownWidget),

    class Meta:
        model = PostQuestion
        fields = ('title', 'text_content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostAnswer
        fields = ('text_content',)
