from django.contrib import admin
from django.urls import path,include
from django.conf.urls import  url
import home.urls
import member.urls
import article.urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home,name="home"),    
    path('home/',include(home.urls)),
    path('member/',include(member.urls)),
    path('article/',include(article.urls)),
    path('api/', include('api.urls')),
    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
