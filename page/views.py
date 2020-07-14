from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView
from .models import PostQuestion, PostAnswer
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from taggit.models import Tag
from .forms import PostForm, CommentForm


class Index(ListView):
    queryset = PostQuestion.objects.all()
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 3


def detail(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    context = {'post': post}
    return render(request, 'detail.html', context)


"""def add_comment_to_post(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post', {'form': form})"""


# @permission_required('Polls', raise_exception=True)
@login_required
def ask(request):
    """ unless user is logged then open """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'ask.html', {'form': form})


"""def edit(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return redirect('/', + post.slug)
    else:
        form = PostForm()
    return render(request, 'ask')"""
