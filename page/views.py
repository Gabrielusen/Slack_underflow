from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import PostQuestion, PostAnswer
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from rest_framework import generics
from .serializers import QuestionSerializer


class Index(ListView):
    queryset = PostQuestion.objects.all()
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 10


def detail(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    return render(request, 'detail.html', {'post': post})


def add_comment(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'form': form})


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


class QuestionEditView(LoginRequiredMixin, UpdateView):
    model = PostQuestion
    template_name = 'edit.html'
    fields = ('title', 'text_content',)

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = PostQuestion
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# @permission_required('Polls', raise_exception=True)
@login_required()
def delete(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    if request.method == 'POST':
        post.user = request.user
        post.delete()
        return redirect('/')
    context = {}
    return render(request, 'delete.html', context)


class APIQuestionList(generics.ListCreateAPIView):
    queryset = PostQuestion.objects.all()
    serializer_class = QuestionSerializer


class APIQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostQuestion.objects.all()
    serializer_class = QuestionSerializer
