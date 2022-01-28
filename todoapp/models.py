from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    status = models.CharField(max_length=10, choices=(("new", "new"), ("done", "done")))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

