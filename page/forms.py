from django import forms
from .models import PostAnswer, PostQuestion
# from tinymce.widgets import TinyMCE
from pagedown.widgets import PagedownWidget
from django.forms import TextInput


class PostForm(forms.ModelForm):
    # title = forms.CharField(widget=PagedownWidget())
    text_content = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = PostQuestion
        fields = ('title', 'text_content', 'tags',)


class CommentForm(forms.ModelForm):
    text_content = forms.CharField(widget=PagedownWidget(attrs={}))

    class Meta:
        # widget = {'name': TextInput(attrs={'placeholder': 'Type your answer here'})}
        model = PostAnswer
        fields = ('text_content',)


class SearchForm(forms.Form):
    query = forms.CharField()

