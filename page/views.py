from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView
from .models import PostQuestion, PostAnswer
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from taggit.models import Tag
from .forms import PostForm, CommentForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy


class Index(ListView):
    queryset = PostQuestion.objects.all()
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 10


def detail(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    """if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.instance.question = post
            form.instance.user = request.user
            form.save()
            redirect('index')
    else:
        form = CommentForm()"""
    return render(request, 'detail.html', {'post': post})


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


"""class EditView(UpdateView):
    model = PostQuestion
    fields = ('title', 'text_content', 'tags')
    template_name = 'edit.html'"""


"""def edit(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    if request.method == 'POST':
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})"""

