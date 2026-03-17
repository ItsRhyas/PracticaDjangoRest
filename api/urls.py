from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, RegistroAccesoViewSet

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')
router.register(r'accesos', RegistroAccesoViewSet, basename='acceso')

urlpatterns = [
    path('', include(router.urls)),
]