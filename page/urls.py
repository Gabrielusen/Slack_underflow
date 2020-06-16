from .views import ArticleListView, ArticleDetailView
from django.urls import path


urlpatterns = [
    path('<slug:slug>', ArticleDetailView.as_view(), name='detail'),
    path('', ArticleListView.as_view(), name='index'),
]
