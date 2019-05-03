from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from todo_lists.models import TodoList

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(null=True, blank=True)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.text

    def toggle(self):
        self.completed = not self.completed
        if self.completed:
            self.completed_date = timezone.now()
        else:
            self.completed_date = None
        self.save()