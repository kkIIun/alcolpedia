from django.urls import path,include
from . import views


urlpatterns = [
    path('List', views.List, name="List"),
    path('like/<int:content_id>', views.like, name="like"),
    path('cancel/<int:content_id>', views.cancel, name="cancel"),
]