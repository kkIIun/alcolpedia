from django.urls import path,include
from . import views


urlpatterns = [
    path('game', views.list_game, name="game"),
    path('bgm', views.list_bgm, name="bgm"),
    path('alcohol', views.list_alcohol, name="alcohol"),
    path('cheers', views.list_cheers, name="cheers"),
    path('setting', views.list_setting, name="setting"),
    path('like/<int:content_id>', views.like, name="like"),
    path('cancel/<int:content_id>', views.cancel, name="cancel"),
    path('search', views.search, name="search"),
    path('tag/<int:tag_id>', views.tag, name="tag"),
    # path('detail/<int:content_id>', views.detail, name="detail"),
]