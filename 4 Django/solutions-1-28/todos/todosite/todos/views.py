from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test

from todo_lists.models import *
from .models import *

#Custom decorator
def user_owns_todo(func):
    def check_and_call(request, *args, **kwargs):
        #user = request.user
        #print user.id
        pk = kwargs["pk"]
        todo = Todo.objects.get(pk=pk)
        if (todo.user != request.user): 
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return check_and_call


def not_doug(user):
    return not user.username.lower().startswith('doug')


# Create your views here.
@login_required
def index(request, todo_list):
    todo_list = get_object_or_404(TodoList, pk=todo_list, user=request.user)
    todos = Todo.objects.filter(todo_list=todo_list).order_by('-created_date', 'completed')

    context = {
        'todos': todos,
        'title': todo_list.title,
        'todo_list': todo_list.pk
    }
    return render(request, 'todos/index.html', context)


@login_required
# @user_passes_test(not_doug)
def add_todo(request, todo_list):
    if request.method == 'POST':
        # print(request.POST) # request.POST returns a dictionary of post parameters
        # # all inputs from a form are available in it, where the key == input.name
        # create new todo from POST parameters
        text_from_input = request.POST['todo']
        todo_list = get_object_or_404(TodoList, pk=todo_list)
        todo = Todo(text=text_from_input, user=request.user, todo_list=todo_list)
        todo.save()
        return redirect('todos:index', todo_list=todo.todo_list.pk)


@user_owns_todo
def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    # # equivalent to above, but get_obj_or_404 is safer
    # todo = Todo.objects.get(pk=pk)
    todo.toggle()
    return redirect('todos:index', todo_list=todo.todo_list.pk)


@user_owns_todo
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()    
    return redirect('todos:index', todo_list=todo.todo_list.pk)


@user_owns_todo
def edit_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todos = Todo.objects.filter(todo_list=todo.todo_list).order_by('-created_date', 'completed')
    return render(request, 'todos/index.html', {
        'todos': todos, 
        'pk': pk, 
        'editing': True,
        'todo_list': todo.todo_list.pk
    })

@user_owns_todo
def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        text_from_input = request.POST['todo']
        todo.text = text_from_input
        todo.save()
    return redirect('todos:index', todo_list=todo.todo_list.pk)
