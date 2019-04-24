# urls.py
from django.urls import path
from . import views

app_name = 'todos' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('todos/add', views.add_todo, name='add_todo'),
    path('todos/<int:pk>/toggle', views.toggle_todo, name='toggle_todo'),
    path('todos/<int:pk>/delete', views.delete_todo, name='delete_todo'),
    path('todos/<int:pk>/edit', views.edit_todo, name='edit_todo'),
]