from django.db import models
from empleados.models import Empleado


class Contrato(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Contrato de {self.empleado.nombre}"