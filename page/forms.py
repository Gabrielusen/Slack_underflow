from django import forms
from .models import PostAnswer, PostQuestion
from django.db import models
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    class Meta:
        model = PostQuestion
        widget = {
            'meta': forms.Textarea(attrs={'cols': 10, 'rows': 1})
        }
        fields = ('title', 'text_content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostAnswer
        fields = ('text_content',)
