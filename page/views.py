from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import PostQuestion, PostAnswer
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PostForm, CommentForm, SearchForm
from django.contrib.postgres.search import SearchVector
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


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


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = PostQuestion.objects.annotate(
                search=SearchVector('title', 'text_content'),
            ).filter(search=query)
            print(results)
    return render(request,
                  'index.html',
                  {'form': form,
                   'query': query,
                   'results': results})
