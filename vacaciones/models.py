from django.db import models
from empleados.models import Empleado


class Vacacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Vacaciones {self.empleado.nombre}"