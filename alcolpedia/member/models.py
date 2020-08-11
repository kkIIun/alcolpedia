from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profile/",default= '사용자.png')
    
    def __str__(self):
        return self.user.username


@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    
@receiver(post_save, sender = User)
def save_user_profilepost_save(sender, instance, **kwargs):
    instance.profile.save()

# class Bookmark(models.Model):
#     content = models.ForeignKey(Content, on_delete=models.CASCADE)
#     # member = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
