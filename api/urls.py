from django.urls import path, include [cite: 129]
from rest_framework.routers import DefaultRouter [cite: 130]
from .views import VehiculoViewSet, RegistroAccesoViewSet

# Creamos el enrutador [cite: 131]
router = DefaultRouter()

# Registramos los endpoints para Vehículos y Accesos [cite: 132]
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')
router.register(r'accesos', RegistroAccesoViewSet, basename='acceso')

# Definimos urlpatterns incluyendo las rutas del router [cite: 135, 138]
urlpatterns = [
    path('', include(router.urls)),
]