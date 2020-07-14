from django import forms
from .models import PostAnswer, PostQuestion
# from tinymce.widgets import TinyMCE
from pagedown.widgets import PagedownWidget


class PostForm(forms.ModelForm):
    # title = forms.CharField(widget=PagedownWidget())
    text_content = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = PostQuestion
        fields = ('title', 'text_content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostAnswer
        fields = ('text_content',)
