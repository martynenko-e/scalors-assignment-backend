from django.urls import path

from .views import ListBoard, DetailBoard, DetailTodo

urlpatterns = [
    path('board', ListBoard.as_view()),
    path('board/<uuid:pk>/', DetailBoard.as_view(), name='board-detail'),
    path('todo/<uuid:pk>', DetailTodo.as_view(), name='todo-detail'),
]
