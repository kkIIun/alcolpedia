from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.utils import timezone
from django.conf import settings

class Tag(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Content(models.Model):
    SORT = (
        ('bgm','브금'),('setting','옵션'),('game','술게임'),('cheers','건배사'),('alcohol','폭탄주'),
    )
    
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'published'),
        ('w', 'withdrawn')
    )

    title = models.CharField(max_length = 200)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    body = MDTextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add = True)
    tag = models.ManyToManyField(Tag,related_name='hashtag', blank=True)
    like = models.ManyToManyField(User,related_name='likers',blank=True)
    bookmark = models.ManyToManyField(User,related_name='bookmarks',blank=True)
    summary = models.CharField(max_length = 50, blank=True, null=True)
    difficulty = models.IntegerField(null=True,default=1, blank=True)
    image = models.ImageField(upload_to="content/", blank=True, null=True)
    sort = models.CharField(max_length=10,choices=SORT,default='술게임')
    audio = models.FileField(upload_to="audio/", blank = True, null = True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    def __str__(self):
        return self.title + "[" + self.sort + "]"
    
    def like_count(self):
        return self.like.count()

    def bookmark_count(self):
        return self.bookmark.count()

    def get_represent_user(self):
        ret = ""
        if len(self.like.all()) > 0:
            ret = self.like.all()[0].username
        return ret

class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='comments')
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}님이 {self.content}에 단 댓글"