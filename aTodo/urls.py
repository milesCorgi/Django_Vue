from django.conf.urls import url
from aTodo.views import add_todo, show_todos, delete_todo

urlpatterns = [
    url(r'add_todo', add_todo, ),
    url(r'delete_todo', delete_todo, ),
    url('show_todos/', show_todos, ),
]
