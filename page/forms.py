from django import forms
from .models import PostAnswer, PostQuestion


class PostForm(forms.ModelForm):
    class Meta:
        model = PostQuestion
        fields = ['title', 'text_content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostAnswer
        fields = ('text_content',)
