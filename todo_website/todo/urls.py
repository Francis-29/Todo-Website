from django.urls import path
from .views import TodoListView, TodoDeleteView, create


urlpatterns = [
    path('', TodoListView.as_view(), name='todo-home'),
    path('create/', create, name='todo-create'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo-delete'),
]
