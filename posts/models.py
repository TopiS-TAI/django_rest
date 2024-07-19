from django.db import models

# Create your models here.

class Post(models.Model):
    posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    body = models.TextField()

    class Meta:
        ordering = ['posted']
