from django.db import models

# Create your models here.
class Suggetion(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    date = models.DateTimeField()