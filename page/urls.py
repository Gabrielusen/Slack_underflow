from .views import detail, ask, Index, delete, QuestionEditView, QuestionDeleteView
from django.urls import path
from .apiviews import QuestionList, QuestionDetail


urlpatterns = [
    # path('<slug:slug>/comment', add_comment_to_post, name='add_comment_to_post'),
    path('ask/', ask, name='ask'),
    path('<slug:slug>', detail, name='detail_view'),
    path('', Index.as_view(), name='index'),
    path('edit/<slug:slug>/', QuestionEditView.as_view(), name='edit'),
    path('delete/<slug:slug>/', QuestionDeleteView.as_view(), name='delete'),
    # path('edit/<slug:slug>/', edit, name='edit'),
    path('question/', QuestionList.as_view(), name='question_list'),
    path('question/<int:pk>', QuestionDetail.as_view(), name='question_detail')
]
