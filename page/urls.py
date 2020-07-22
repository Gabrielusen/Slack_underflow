from .views import detail, ask, Index, delete, QuestionEditView
from django.urls import path


urlpatterns = [
    # path('<slug:slug>/comment', add_comment_to_post, name='add_comment_to_post'),
    path('ask/', ask, name='ask'),
    path('<slug:slug>', detail, name='detail_view'),
    path('', Index.as_view(), name='index'),
    path('edit/<slug:slug>/', QuestionEditView.as_view(), name='edit'),
    path('delete/<slug:slug>/', delete, name='delete'),
    # path('edit/<slug:slug>/', edit, name='edit'),
]
