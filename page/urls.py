from .views import ArticleListView, detail_view
from django.urls import path


urlpatterns = [
    path('<slug:slug>', detail_view, name='detail'),
    path('', ArticleListView.as_view(), name='index'),
]
