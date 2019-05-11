# urls.py
from django.urls import path, include
from django.views.generic import TemplateView

# imports for rest framework api
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)
router.register(r'todo_lists', views.TodoListViewSet)



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


urlpatterns += [
    path('drf_dashboard/', TemplateView.as_view(template_name='drf/index.html'), name='drf_dashboard'),
    path('drf_dashboard/list/<int:pk>', TemplateView.as_view(template_name='drf/todo_list.html'), name='drf_detail'),
]


# drf api endpoints
urlpatterns += [
    path('drf/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
