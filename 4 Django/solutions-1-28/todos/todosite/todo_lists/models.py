from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(null=True, blank=True)

    # @property
    # def completed(self):
    #     return bool([todo for todo in self.todos if todo.completed])

