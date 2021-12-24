from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rpi/', include('rpi.urls')),
    path('', include('portal.urls')),
]
