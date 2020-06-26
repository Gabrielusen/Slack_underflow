from .views import index, detail
from django.urls import path


urlpatterns = [
    path('<slug:slug>', detail, name='detail_view'),
    path('', index, name='index'),
]
