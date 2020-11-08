from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets, pagination
from .serializers import ProfileSerializer, UserSerializer, ContentSerializer
from member.models import Profile
from article.models import Content
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from article.models import Tag
import json



@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
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
    profile = Profile.objects.filter(user = request.user)
    if request.method == 'GET' :
        profile_serialize = json.loads(serializers.serialize('json', profile))
        bookmarks = Content.objects.filter(bookmark__id = request.user.id)
        bookmark_list = json.loads(serializers.serialize('json', bookmarks)) 
        profile_serialize[0] = [profile_serialize[0], bookmark_list]
        # print(profile_serialize[0][1][1]['fields']['title']) 
        return HttpResponse(json.dumps(profile_serialize), content_type="text/json-comment-filtered")
    # elif request.method == 'PUT' :
    #     serializer = ProfileSerializer(profile ,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return HttpResponse(serializer, content_type="text/json-comment-filtered")

@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def tag_function(request):
    tags = Tag.objects.all()
    tags = serializers.serialize('json', tags)
    return HttpResponse(tags, content_type="text/json-comment-filtered")
# def comment_create(request, music_id):
#     serializer = ProfileSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(music_id=music_id)
#         return Response(serializer.data)


