from django.contrib.auth.models import User
from rest_framework import serializers

from member.models import Profile
from article.models import Content, Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'avatar')

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('sort','title', 'body','tag','difficulty','like','bookmark','updated_at','summary','image','audio')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["title"]