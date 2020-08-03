from django.urls import path,include
from . import views


urlpatterns = [
    path('List', views.List, name="List"),
]