from django.shortcuts import render, get_object_or_404

# drf imports
from rest_framework import viewsets
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from todos.models import *
from todo_lists.models import *

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly,)


    def get_queryset(self):
        """
        defines what is returned when you send a GET request to this API endpoint
        """
        return Todo.objects.filter(user=self.request.user)

    def get_object(self):
        """
        defines what is returned when we access a single todo object.
        this checks if the user has the permissions to modify the object (i.e. make 
        POST/PUT/PATCH/DELETE requests), or otherwise is read-only (only GET/HEAD/OPTIONS).
        """
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        """
        a todo needs to have a user and todo_list field to be saved, so we'll manually
        set those here.

        the todo_list pk is being passed in as json data. we access it through request.data
        """
        todo_list = get_object_or_404(TodoList, pk=self.request.data['todo_list'])
        return serializer.save(user=self.request.user, todo_list=todo_list)



class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        """
        defines what is returned when you send a GET request to this API endpoint
        """        
        return TodoList.objects.filter(user=self.request.user)

    def get_object(self):
        """
        defines what is returned when we access a single todo object.
        this checks if the user has the permissions to modify the object (i.e. make 
        POST/PUT/PATCH/DELETE requests), or otherwise is read-only (only GET/HEAD/OPTIONS).
        """
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        """
        a todolist needs to have a user foreign key set 

        we can grab that from the request, which drf automatically sets as a property
        """
        return serializer.save(user=self.request.user)
