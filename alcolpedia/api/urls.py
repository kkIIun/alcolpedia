from django.conf.urls import  url, include
from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path("articles/", views.contents_function, name = "articles"),
    path("profile/", views.profile_function, name = "profile"),
    path("tag/", views.tag_function, name = "tag"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]