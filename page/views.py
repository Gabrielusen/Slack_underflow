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
    paginate_by = 10


def detail(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    comments = post.objects.filter(approved_comment=True)
    new_comment = None
    #  comment posted
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()
    context = {'post': post,
               'comments': comments,
               'new_comment': new_comment,
               'form': form}
    return render(request, 'detail.html', context)


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
