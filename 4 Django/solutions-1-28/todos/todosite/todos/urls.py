# urls.py
from django.urls import path
from . import views

app_name = 'todos' # for namespacing
urlpatterns = [
    path('<int:todo_list>', views.index, name='index'),
    path('<int:todo_list>/add', views.add_todo, name='add'),
    path('<int:pk>/toggle', views.toggle_todo, name='toggle'),
    path('<int:pk>/delete', views.delete_todo, name='delete'),
    path('<int:pk>/edit', views.edit_todo, name='edit'),
    path('<int:pk>/editing', views.edit_view, name='edit_view'),
]
