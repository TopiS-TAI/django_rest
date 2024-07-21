from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['posted']
