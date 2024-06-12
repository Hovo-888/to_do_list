
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/todos/', views.todo_list_api, name='todo_list_api'),
    path('api/todos/create/', views.todo_create_api, name='todo_create_api'),
    path('api/todos/update/<int:id>/', views.todo_update_api, name='todo_update_api'),
    path('api/todos/delete/<int:id>/', views.todo_delete_api, name='todo_delete_api'),
]