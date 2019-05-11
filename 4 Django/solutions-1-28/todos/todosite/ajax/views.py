from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
import json

from todo_lists.models import *
from todos.models import *


def todo_lists(request):
    if request.method == 'GET':
        todo_lists = TodoList.objects.filter(user=request.user).order_by('-created_date')
        data = serialize('json', todo_lists)
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        # print(type(request.body), request.body)
        body = json.loads(request.body)
        # create new todo list
        todo_title = body['todo_list']
        todo_list = TodoList(user=request.user, title=todo_title)
        todo_list.save()
        return HttpResponse('Success')


def todo_list(request, todo_list):
    todo_list = get_object_or_404(TodoList, pk=todo_list, user=request.user)
    todos = Todo.objects.filter(todo_list=todo_list)
    if request.method == 'GET':
        # read todo_list
        data = {
            'pk': todo_list.pk,
            'title': todo_list.title,
            'user': serialize('json', [todo_list.user], fields='username'),
            'created_date': todo_list.created_date,
            'completed_date': todo_list.completed_date,
            'todos': serialize('json', todos)
        }
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        # create todo
        body = json.loads(request.body)
        text = body['todo']
        todo = Todo(text=text, user=request.user, todo_list=todo_list)
        todo.save()

    elif request.method == 'DELETE':
        # delete todo_list
        todo_list.delete()
    
    return HttpResponse('Success')
        

def todo(request, todo_list, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'GET':
        # read todo
        response = serialize('json', todo) 
        return JsonResponse(response, safe=False)

    elif request.method == 'PUT':
        # toggle and edit todo
        body = json.loads(request.body)

        if body.get('toggle'):
            # toggle todo
            todo.toggle()

        if body.get('todo'):
            # edit todo
            text = body['todo']
            # print('editing todo:', text)
            todo.text = text
            todo.save()

    elif request.method == 'DELETE':
        # delete todo
        todo.delete()

    return HttpResponse('Success')

