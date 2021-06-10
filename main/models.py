from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    agree = models.BooleanField(default=False)
    on_time = models.DateTimeField(auto_now_add=True)
    minutes = models.FloatField(default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
