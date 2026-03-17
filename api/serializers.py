from rest_framework import serializers
from .models import Vehiculo, RegistroAcceso

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class RegistroAccesoSerializer(serializers.ModelSerializer):
    # Esto mostrará la placa en lugar de solo el ID del vehículo al consultar registros
    placa_vehiculo = serializers.ReadOnlyField(source='vehiculo.placa')

    class Meta:
        model = RegistroAcceso
        fields = '__all__'