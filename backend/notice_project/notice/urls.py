from django.urls import path
from .views import CreateNoticeView, CommentReactionAPIView, AllNoticesView, delete, deleteNotice

#add url routes here

urlpatterns = [

    path('notices/', CreateNoticeView.as_view()),

    path('all-notices', AllNoticesView.as_view()),

    path('comment/reaction/update', CommentReactionAPIView.as_view()),
    
    path('delete/', delete, name="delete"),

      path('delete-notice', deleteNotice, name='delete-notice'),
]
