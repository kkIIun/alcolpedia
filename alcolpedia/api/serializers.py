from django.contrib.auth.models import User
from rest_framework import fields
from rest_framework.serializers import SerializerMetaclass
from member.models import Profile
from article.models import Content
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'avatar', 'location')

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('title', 'body')