from todo import views
from django.urls import path

urlpatterns = [
    path("", views.todo_list, name = 'todo-list'), # To display in home url
    path("todo-create/", views.todo_create, name = 'todo-create'),
    path('todo/<int:pk>/', views.todo_detail, name='todo'),
    path("todo-delete/<int:pk>/", views.todo_delete, name = 'todo-delete'),
    path("todo-update/<int:pk>/", views.todo_update, name = 'todo-update'),
    # path('todo-reorder/', views.todo_reorder, name='todo-reorder'),
]