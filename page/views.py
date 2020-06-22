from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
from .models import PostQuestion
from django.db.models import Q
# from django.contrib.auth.decorators import login_required


class ArticleListView(ListView):
    model = PostQuestion
    template_name = 'index.html'
    paginate_by = 10


class ArticleDetailView(DetailView):
    model = PostQuestion
    template_name = 'detail.html'
    # context_object_name = 'questions'


class SearchResultsView(ListView):
    model = PostQuestion
    template_name = 'search_results.html'

    def get_queryset(self):
        return PostQuestion.objects.filter(
            Q(title__icontains='first note') | Q(slug__icontains='second-note')
        )
