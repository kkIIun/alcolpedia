from django.contrib import admin
from django.urls import path,include
import home.urls
import member.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home,name="home"),    
    path('home/',include(home.urls)),
    path('member/',include(member.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
