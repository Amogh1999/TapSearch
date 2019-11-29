from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import tapsearch.settings

urlpatterns = [ 
    path('',include('home.urls')),
    path('api/',include('api.urls')),
    path('admin/', admin.site.urls),
]
