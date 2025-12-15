from django.db import models
from departamentos.models import Departamento
from puestos.models import Puesto


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"