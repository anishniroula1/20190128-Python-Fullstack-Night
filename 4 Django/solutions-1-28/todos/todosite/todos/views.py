from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('-created_date', 'completed')
    return render(request, 'todos/index.html', {'todos': todos})

def add_todo(request):
    # print(request)
    # print(request.POST)
    if request.method == 'POST':
        # create new todo from POST parameters
        text_from_input = request.POST['todo']
        todo = Todo(text=text_from_input)
        todo.save()
    return redirect('todos:index')

def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    # # equivalent to above, but get_obj_or_404 is safer
    # todo = Todo.objects.get(pk=pk)
    todo.toggle()
    return HttpResponse('success')

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()    
    return HttpResponse('success')

def edit_todo(request, pk):
    pass