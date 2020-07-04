from django.urls import path

from .views import ListBoard, DetailBoard, DetailTodo, ListTodo


urlpatterns = [
    path('boards/', ListBoard.as_view(), name='boards'),
    path('boards/<uuid:pk>/', DetailBoard.as_view(), name='board-detail'),
    path('todos/', ListTodo.as_view(), name='todos'),
    path('todos/<uuid:pk>/', DetailTodo.as_view(), name='todo-detail'),
    
]
