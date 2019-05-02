from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('-created_date', 'completed')
    pi = 3.14
    context = {'todos': todos}
    return render(request, 'todos/index.html', context)

def add_todo(request):
    if request.method == 'POST':
        # print(request.POST) # request.POST returns a dictionary of post parameters
        # # all inputs from a form are available in it, where the key == input.name
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
    return redirect('todos:index')

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()    
    return redirect('todos:index')

def edit_view(request, pk):
    todos = Todo.objects.all().order_by('-created_date', 'completed')
    # todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todos/index.html', {
        'todos': todos, 
        'pk': pk, 
        'editing': True
    })


def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        text_from_input = request.POST['todo']
        todo.text = text_from_input
        todo.save()
    return redirect('todos:index')
