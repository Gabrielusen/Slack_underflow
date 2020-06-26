from .views import ArticleListView, CommentCreateView
from django.urls import path


urlpatterns = [
    path('<slug:slug>', CommentCreateView.as_view(), name='detail_view'),
    path('', ArticleListView.as_view(), name='index'),
]
