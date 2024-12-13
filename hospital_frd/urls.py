# hospital/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('urgencias/', include('urgencias.urls')),  # Incluimos las URLs de la app 'urgencias'
    path('', include('urgencias.urls')),  # Ruta vacía, redirige a 'urgencias.urls'
]
