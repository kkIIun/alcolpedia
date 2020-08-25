from django.urls import path,include
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.table_contents, name = "article"),
    # path('like/<int:content_id>', views.like, name="like"),
    re_path(r'^like/$', views.like, name='like'),
    path('tag/<int:tag_id>', views.tag, name="tag"),
    path('detail/<int:content_id>', views.detail, name="detail"),
    path('filter', views.filter, name="filter"),
    re_path(r'^bookmark/$', views.bookmark, name='bookmark'),
]