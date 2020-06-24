from django import forms
from .models import PostAnswer


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostAnswer
        fields = ('user', 'text_content')
