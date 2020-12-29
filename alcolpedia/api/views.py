from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets, pagination
from .serializers import TagSerializer, ContentSerializer
from member.models import Profile
from article.models import Content
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from article.models import Tag
from django.contrib.auth.decorators import login_required
import json
from django.contrib import auth

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def contents_function(request):
    if request.method == 'GET' :
        name= request.GET.get('name')
        # contents = Content.objects.filter(updated_at__isnull=False).order_by('updated_at')
        contents = Content.objects.filter(sort = name)
        serializer = ContentSerializer(contents, many= True)
        return Response(serializer.data)
        # content_list = json.loads(serializers.serialize('json', contents)) 
        # return HttpResponse(json.dumps(content_list), content_type="text/json-comment-filtered")


@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def profile_function(request):
    if request.method == 'GET' :
        profile = Profile.objects.filter(user = request.user)
        profile_serialize = json.loads(serializers.serialize('json', profile))
        bookmarks = Content.objects.filter(bookmark__id = request.user.id)
        bookmark_list = json.loads(serializers.serialize('json', bookmarks)) 
        profile_serialize[0] = [profile_serialize[0], bookmark_list]
        profile_serialize[0][0]['fields']['user'] = request.user.username
        return HttpResponse(json.dumps(profile_serialize), content_type="text/json-comment-filtered")
    
    if request.method == 'PUT' :
        profile = get_object_or_404(Profile,user__username = request.user.username)
        user = get_object_or_404(User, pk = request.user.id)
        username = request.GET.get('username')
        image = request.FILES.get('image')
        if username:
            user.username = username
        if image:
            profile.avatar = image
        user.save()
        profile.save()

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def tag_function(request):
    queryset = Tag.objects.all()
    serializer = TagSerializer(queryset, many=True)
    return Response(data=serializer.data)            
# login, logout, registration 은 rest-auth를 사용
    