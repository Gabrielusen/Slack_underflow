from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import PostQuestion


class ArticleListView(ListView):
    model = PostQuestion
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = PostQuestion
    template_name = 'detail.html'
    # context_object_name = 'questions'
