from django.conf.urls import  url, include
from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path("articles/", views.contents_function, name = "api_articles"),
    path("profile/", views.profile_function, name = "api_profile"),
    path("tag/", views.tag_function, name = "api_tag"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]