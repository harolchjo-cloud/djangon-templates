from django.db import models
from empleados.models import Empleado
from beneficios.models import Beneficio


class BeneficioEmpleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    beneficio = models.ForeignKey(Beneficio, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()

    def __str__(self):
        return f"{self.beneficio.nombre} para {self.empleado.nombre}"
