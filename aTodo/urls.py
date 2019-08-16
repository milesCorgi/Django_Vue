from django.urls import path
from aTodo.views import add_todos, show_todos, delete_todos, edit_todos, search_todos

urlpatterns = [
    path(r'add_todos', add_todos, ),
    path(r'search_todos', search_todos, ),
    path(r'delete_todos', delete_todos, ),
    path('show_todos/', show_todos, ),
    path('edit_todos/<int:todo_id>', edit_todos, ),
]
