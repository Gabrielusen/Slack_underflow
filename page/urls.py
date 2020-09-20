from .views import (
    detail,
    ask,
    Index,
    QuestionEditView,
    QuestionDeleteView,
    APIQuestionDetail,
    APIQuestionList,
)
from django.urls import path


urlpatterns = [
    # path('<slug:slug>/comment', add_comment_to_post, name='add_comment_to_post'),
    path('ask/', ask, name='ask'),
    path('<slug:slug>', detail, name='detail_view'),
    path('', Index.as_view(), name='index'),
    path('edit/<slug:slug>/', QuestionEditView.as_view(), name='edit'),
    path('delete/<slug:slug>/', QuestionDeleteView.as_view(), name='delete'),
    # path('edit/<slug:slug>/', edit, name='edit'),
    path('question/', APIQuestionList.as_view()),
    path('question/<int:pk>', APIQuestionDetail.as_view()),
]
