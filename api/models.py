from django.db import models

class Vehiculo(models.Model):
    placa = models.CharField(max_length=15, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.placa} - {self.marca}"

class RegistroAcceso(models.Model):
    # Relación con Vehiculo: si se borra el vehículo, se borran sus registros
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='accesos')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    tipo_acceso = models.CharField(max_length=10, choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')])
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.vehiculo.placa} | {self.tipo_acceso} | {self.fecha_hora}"