from django.db import models

# The User model is provided by Django's built-in authentication system,
# which we'll use to associate the to-do items with the logged-in user.
from django.contrib.auth.models import User

# Create your models here.

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_item = models.TextField()

    def __str__(self):
        return self.todo_item

