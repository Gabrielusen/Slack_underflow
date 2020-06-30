from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from .models import PostQuestion, PostAnswer
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from .forms import PostForm
from django.template.defaultfilters import slugify


def index(request):
    posts = PostQuestion.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def detail(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    context = {'post': post}
    return render(request, 'detail.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # filter questions by tag name
    post = PostQuestion.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'post': post
    }
    return render(request, 'index.html', context)


def ask(request, pk):
    post = PostAnswer.objects.all()
    context = {'post': post}
    return render(request, 'ask.html', context)


"""class SearchResultsView(ListView):
    model = PostQuestion
    template_name = 'search_results.html'

    def get_queryset(self):
        return PostQuestion.objects.filter(
            Q(title__icontains='first note') | Q(slug__icontains='second-note')
        )"""
