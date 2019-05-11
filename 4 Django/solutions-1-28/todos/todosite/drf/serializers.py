# serializers.py
from rest_framework import serializers
from todos.models import Todo
from todo_lists.models import TodoList

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    todo_list = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='drf:todolist-detail'
    )
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'text', 'completed', 'created_date', 'completed_date', 'todo_list', 'user')


class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)
    # todos = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='ajax:todo-detail'
    # )
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TodoList
        fields = ('id', 'user', 'title', 'created_date', 'completed_date', 'todos')
