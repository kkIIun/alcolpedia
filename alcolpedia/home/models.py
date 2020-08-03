from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.utils import timezone
# from member.models import Profile

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title


class Content(models.Model):
    title = models.CharField(max_length = 200)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    body = MDTextField()
    dated_at = models.DateTimeField(auto_now_add = True)
    tag = models.ManyToManyField(Tag,related_name='hashtag')
    like = models.ManyToManyField(User,related_name='likers',blank=True)
    summary = models.CharField(max_length = 50)
    difficulty = models.IntegerField(null=True,default=0)
    image = models.ImageField(upload_to="content/", blank=True, null=True)
    # intro = models.AutoField()

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    # member = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    