# urls.py
from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'ajax' # for namespacing
urlpatterns = [
    path('', TemplateView.as_view(template_name='ajax/index.html'), name='dashboard'),
    path('todo_list/<int:pk>', TemplateView.as_view(template_name='ajax/todo_list.html'), name='detail'),
]

# handmade api endpoints
urlpatterns += [
    path('api/todo_lists/', views.todo_lists, name='todo_lists'),
    path('api/todo_list/<int:todo_list>/', views.todo_list, name='todo_list'),
    path('api/todo_list/<int:todo_list>/<int:pk>', views.todo, name='todo'),
]