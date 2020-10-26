from django.urls import path
from .views import QuestionList, QuestionDetail


app_name = 'page'

urlpatterns = [
    path('questions/', QuestionList.as_view(), name='question_list'),
    path('questions/<pk>/', QuestionDetail.as_view(), name='question_detail'),
]
