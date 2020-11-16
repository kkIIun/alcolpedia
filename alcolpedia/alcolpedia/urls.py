from django.contrib import admin
from django.urls import path,include
from django.conf.urls import  url
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
import home.urls
import member.urls
import article.urls
import api.urls
import suggestion.urls
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home,name="home"),    
    path('home/',include(home.urls)),
    path('member/',include(member.urls)),
    path('article/',include(article.urls)),
    path('suggestion/',include(suggestion.urls)),
    path('api/', include(api.urls)),
    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api_auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('mdeditor/', include('mdeditor.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
