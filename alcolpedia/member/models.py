from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
