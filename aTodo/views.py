from django.core import serializers
import json
from django.http import JsonResponse
from django.shortcuts import render
from aTodo.models import Todo
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# Create your views here.
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def add_todo(request):
    response = {}
    try:
        todo = Todo(Todo_body=request.POST.get('Todo_body'))
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
        todo = Todo.objects.filter(Todo_body=request.POST.get('Todo_body'))
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

@csrf_exempt
def edit_todos(request, todo_id):
    response = {}
    if request.method == "GET":
        try:
            todo = Todo.objects.filter(id = todo_id)
            print(todo)
            response['list'] = json.loads(serializers.serialize("json", todo))
            response['msg'] = 'success'
            response['error_num'] = 0
        except  Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
        return JsonResponse(response)
    else:
        try:
            todo = Todo.objects.get(id=todo_id)
            print(request.POST.get('Todo_body'))
            todo.Todo_body = request.POST.get('Todo_body')
            # todo.update_time = request.POST.get('Todo_body')
            todo.save()
            response['msg'] = 'success'
            response['error_num'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1

        return JsonResponse(response)