from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)