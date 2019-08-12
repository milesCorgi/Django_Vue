from django.urls import path
from aTodo.views import add_todo, show_todos, delete_todo, edit_todos

urlpatterns = [
    path(r'add_todo', add_todo, ),
    path(r'delete_todo', delete_todo, ),
    path('show_todos/', show_todos, ),
    path('edit_todos/<int:todo_id>/', edit_todos, ),
]
