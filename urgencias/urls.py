# urgencias/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('ingresar/', views.ingresar_paciente, name='ingresar_paciente'),
    path('paciente_guardado/', views.paciente_guardado, name='paciente_guardado'),
    path('', views.pagina_principal, name='pagina_principal'),  # Página principal
    path('buscar/', views.buscar_paciente, name='buscar_paciente'),  # Ruta de búsqueda
]