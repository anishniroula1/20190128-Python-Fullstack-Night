from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse('pls work')

def add_todo(request):
    pass

def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    # todo = Todo.objects.get(pk=pk)
    todo.toggle()
    return HttpResponse('success')

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()    
    return HttpResponse('success')

def edit_todo(request, pk):
    pass