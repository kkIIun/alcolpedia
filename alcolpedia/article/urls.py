from django.urls import path,include
from . import views

urlpatterns = [
    path('game', views.game, name="game"),
    path('bgm', views.bgm, name="bgm"),
    path('alcohol', views.alcohol, name="alcohol"),
    path('cheers', views.cheers, name="cheers"),
    path('setting', views.setting, name="setting"),
    path('like/<int:content_id>', views.like, name="like"),
    path('cancel/<int:content_id>', views.cancel, name="cancel"),
    path('tag/<int:tag_id>', views.tag, name="tag"),
]