from django.contrib import admin [cite: 142]
from django.urls import path, include [cite: 143]

urlpatterns = [
    path('admin/', admin.site.urls), [cite: 145]
    # Esta línea conecta tu app 'api' con el prefijo /api/ [cite: 146]
    path('api/', include('api.urls')), 
]