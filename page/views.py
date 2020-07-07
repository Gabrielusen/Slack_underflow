from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView
from .models import PostQuestion, PostAnswer
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from taggit.models import Tag
from .forms import PostForm, CommentForm
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


"""def index(request):
    posts = PostQuestion.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)"""


class Index(ListView):
    queryset = PostQuestion.objects.all()
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 10


def detail(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    comments = post.comments.filter(active=True).order_by('created_on')
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = form.save(commit=False)
            # Assign the current post to the comment
            new_comment.question = post
            # Save the comment to the database
            new_comment.save()
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comment': comments,
        'new_comment': new_comment,
        'form': form,
    }
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
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'ask.html', {'form': form})
