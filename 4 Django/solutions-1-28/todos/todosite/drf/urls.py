# urls.py
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

# drf import
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet, 'todo')
router.register(r'todo_lists', views.TodoListViewSet, 'todolist')

app_name = 'drf' # for namespacing
urlpatterns = [
    path('', TemplateView.as_view(template_name='drf/index.html'), name='dashboard'),
    path('list/<int:pk>', TemplateView.as_view(template_name='drf/todo_list.html'), name='detail'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
]
