# urls.py
from django.urls import path
from . import views

app_name = 'todo_lists' # for namespacing
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('list/add', views.add_todo_list, name='add'),
    path('list/<int:pk>', views.todo_list, name='detail'),
    path('list/<int:pk>/delete', views.delete_todo_list, name='delete'),
]