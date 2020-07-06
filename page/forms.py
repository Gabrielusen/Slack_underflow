from django import forms
from .models import PostAnswer, PostQuestion


class PostForm(forms.ModelForm):
    """ Form class for posting questions"""
    # question = forms.CharField(max_length=200)
    # text_content = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = PostQuestion
        fields = ['title', 'text_content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostAnswer
        fields = ['text_content']
