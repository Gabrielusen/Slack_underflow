from .views import index, detail, ask
from django.urls import path


urlpatterns = [
    path('ask/', ask, name='ask'),
    path('<slug:slug>', detail, name='detail_view'),
    path('', index, name='index'),
]
