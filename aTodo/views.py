from django.core import serializers
import json
from django.http import JsonResponse
from django.shortcuts import render
from aTodo.models import Todo

# Create your views here.
# Create your views here.
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def add_todo(request):
    response = {}
    try:
        todo = Todo(Todo_name=request.POST.get('Todo_name'))
        todo.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def delete_todo(request):
    response = {}
    try:
        todo = Todo.objects.filter(Todo_name=request.POST.get('Todo_name'))
        todo.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_todos(request):
    response = {}
    try:
        todos = Todo.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", todos))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
