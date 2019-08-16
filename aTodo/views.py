from django.core import serializers
import json
from django.http import JsonResponse
import datetime
from django.shortcuts import render
from aTodo.models import Todo
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# Create your views here.
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
@csrf_exempt
def add_todos(request):
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

@csrf_exempt
def delete_todos(request):
    response = {}
    try:
        todo = Todo.objects.filter(id=request.POST.get('Todo_id'))
        todo.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
@csrf_exempt
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
def search_todos(request):
    response = {}
    if request.method == "POST":
        try:
            search_start_time = request.POST.get('search_range[0]')
            search_end_time = request.POST.get('search_range[1]')
            print()
            print(request.POST.get('search_range[1]'))
            todo_out_put_id = []
            for todo in Todo.objects.filter().values('id', 'add_time'):
                todo_add_time = str(todo['add_time'])
                todo_add_time = todo_add_time[:todo_add_time.index('.')]
                print(todo_add_time)
                if todo_add_time >= search_start_time and todo_add_time <= search_end_time:
                    todo_out_put_id.append(todo['id'])
            print(todo_out_put_id)
            todos = Todo.objects.filter(id__in=todo_out_put_id)
            response['list'] = json.loads(serializers.serialize("json", todos))
            # print(response['list'])
            response['msg'] = 'success'
            response['error_num'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1

        return JsonResponse(response)

@csrf_exempt
def edit_todos(request, todo_id):
    response = {}
    if request.method == "GET":
        try:
            todo = Todo.objects.filter(id = todo_id)
            # print(todo.add_time.year())
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