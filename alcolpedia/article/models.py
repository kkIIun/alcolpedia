from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.utils import timezone

class Tag(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Content(models.Model):
    SORT = (
        ('bgm','브금'),('setting','옵션'),('game','술게임'),('cheers','건배사'),('alcohol','폭탄주'),
    )
    title = models.CharField(max_length = 200)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    body = MDTextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add = True)
    tag = models.ManyToManyField(Tag,related_name='hashtag', blank=True)
    like = models.ManyToManyField(User,related_name='likers',blank=True)
    summary = models.CharField(max_length = 50, blank=True, null=True)
    difficulty = models.IntegerField(null=True,default=0, blank=True)
    image = models.ImageField(upload_to="content/", blank=True, null=True)
    sort = models.CharField(max_length=10,choices=SORT,default='술게임')
    audio = models.FileField(upload_to="audio/", blank = True, null = True)

    def __str__(self):
        return self.title

    
    def like_count(self):
        return self.like.count()


    def get_represent_user(self):
        ret = ""
        if len(self.like.all()) > 0:
            ret = self.like.all()[0].username
        return ret