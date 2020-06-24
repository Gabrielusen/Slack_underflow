from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
from .models import PostQuestion
from django.db.models import Q
# from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import CommentForm


class ArticleListView(ListView):
    model = PostQuestion
    template_name = 'index.html'
    paginate_by = 10


def detail_view(request, slug):
    post = get_object_or_404(PostQuestion, slug=slug)
    # list of active comments for this post
    comment = post.comments.filter(is_anonymous=True)
    new_comment = None

    if request.method == 'POST':
        # a comment was posted
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # create comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'detail.html',
                  {'post': post,
                   'comment': comment,
                   'new_comments': new_comment,
                   'comment_form': comment_form})


"""class ArticleDetailView(DetailView):
    model = PostQuestion
    template_name = 'detail.html'
    # context_object_name = 'questions'"""


"""class SearchResultsView(ListView):
    model = PostQuestion
    template_name = 'search_results.html'

    def get_queryset(self):
        return PostQuestion.objects.filter(
            Q(title__icontains='first note') | Q(slug__icontains='second-note')
        )"""
