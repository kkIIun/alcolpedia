from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.table_contents, name = "article"),
    path('like/<int:content_id>', views.like, name="like"),
    path('cancel/<int:content_id>', views.cancel, name="cancel"),
    path('tag/<int:tag_id>', views.tag, name="tag"),
    path('detail/<int:content_id>', views.detail, name="detail"),
    path('filter', views.filter, name="filter"),
]