from django.shortcuts import render
from rest_framework import viewsets, pagination
from .serializers import ProfileSerializer, UserSerializer, ContentSerializer
from member.models import Profile
from article.models import Content
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def contents_function(request):
    contents = Content.objects.filter(updated_at__isnull=False).order_by('updated_at')
    content_list = serializers.serialize('json', contents)
    return HttpResponse(content_list, content_type="text/json-comment-filtered")