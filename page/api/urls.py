from django.urls import path
from .views import QuestionList, QuestionDetail


app_name = 'page'

urlpatterns = [
    path('question', QuestionList.as_view(), name='question_list'),
    path('question/<pk>', QuestionDetail.as_view(), name='question_detail')
]
