from django import forms
from .models import PostAnswer, PostQuestion


class PostForm(forms.ModelForm):
    question = forms.CharField(max_length=200)
    text_content = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = PostQuestion
        fields = ['question', 'text_content', 'tags']
