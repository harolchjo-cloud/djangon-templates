from django.db import models
from empleados.models import Empleado


class Asistencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Asistencia {self.empleado.nombre} - {self.fecha}"