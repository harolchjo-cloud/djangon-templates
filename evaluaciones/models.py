from django.db import models
from empleados.models import Empleado


class Evaluacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentarios = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Evaluación {self.empleado.nombre}"
