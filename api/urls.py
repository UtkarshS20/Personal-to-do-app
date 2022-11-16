from django.urls import path
from .views import TaskListView , TaskDetailView , taskUpdate
urlpatterns=[
    path('tasks/',TaskListView.as_view()),
    path('tasks/<int:pk>',TaskDetailView.as_view()),
    path('tasks-update/<int:pk>',taskUpdate),
]