from django.urls import path
from .views.project import ProjectDetailView
from .views.task import TaskDetailView

urlpatterns = [
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('projects/<int:pk>/', ProjectDetailView.as_view()),

]
