from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import *

#Custom decorator
def user_owns_list(func):
    def check_and_call(request, *args, **kwargs):
        #user = request.user
        #print user.id
        pk = kwargs["pk"]
        todo = TodoList.objects.get(pk=pk)
        if (todo.user != request.user): 
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return check_and_call


def index(request):
    if request.user.is_authenticated:
        todo_lists = TodoList.objects.filter(user=request.user).order_by('-created_date')
    else:
        todo_lists = []
    context = {'lists': todo_lists}
    return render(request, 'todo_lists/index.html', context)


@user_owns_list
def todo_list(request, pk):
    todo_list = get_object_or_404(TodoList, pk=pk)
    return redirect('todos:index', todo_list=pk)


@login_required
def add_todo_list(request):
    if request.method == 'POST':
        print(request.POST) # request.POST returns a dictionary of post parameters
        # # all inputs from a form are available in it, where the key == input.name
        # create new todo from POST parameters
        text_from_input = request.POST['todo_list']
        todo_list = TodoList(title=text_from_input, user=request.user)
        todo_list.save()
    return redirect('todo_lists:dashboard')


@user_owns_list
def delete_todo_list(request, pk):
    todo_list = get_object_or_404(TodoList, pk=pk)
    todo_list.delete()    
    return redirect('todo_lists:dashboard')

