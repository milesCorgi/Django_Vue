from django.conf.urls import url
from aTodo.views import add_todo, show_todos

urlpatterns = [
    url(r'add_todo', add_todo, ),
    url('show_todos/', show_todos, ),
]
