from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView
from .models import PostQuestion, PostAnswer
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from taggit.models import Tag
from .forms import PostForm
from django.template.defaultfilters import slugify
from django.contrib import messages


def index(request):
    posts = PostQuestion.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


def detail(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    context = {'post': post}
    return render(request, 'detail.html', context)


"""def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # filter questions by tag name
    post = PostAnswer.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'post': post
    }
    return render(request, 'index.html', context)"""


# @permission_required('Polls', raise_exception=True)
@login_required
def ask(request):
    """ unless user is logged then open """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['title'])
            tag = form.save(commit=False)
            tag.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'ask.html', {'form': form})


"""class SearchResultsView(ListView):
    model = PostQuestion
    template_name = 'search_results.html'

    def get_queryset(self):
        return PostQuestion.objects.filter(
            Q(title__icontains='first note') | Q(slug__icontains='second-note')
        )"""
