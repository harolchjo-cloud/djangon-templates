from rest_framework import viewsets
from departamentos.models import Departamento
from puestos.models import Puesto
from empleados.models import Empleado
from contratos.models import Contrato
from asistencias.models import Asistencia
from vacaciones.models import Vacacion
from nominas.models import Nomina
from evaluaciones.models import Evaluacion
from beneficios.models import Beneficio
from beneficios_empleados.models import BeneficioEmpleado
from .serializers import (
    EmpleadoSerializer, DepartamentoSerializer, PuestoSerializer,
    ContratoSerializer, AsistenciaSerializer, VacacionSerializer,
    NominaSerializer, EvaluacionSerializer, BeneficioSerializer,
    BeneficioEmpleadoSerializer
)

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class PuestoViewSet(viewsets.ModelViewSet):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

class VacacionViewSet(viewsets.ModelViewSet):
    queryset = Vacacion.objects.all()
    serializer_class = VacacionSerializer

class NominaViewSet(viewsets.ModelViewSet):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializer

class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

class BeneficioViewSet(viewsets.ModelViewSet):
    queryset = Beneficio.objects.all()
    serializer_class = BeneficioSerializer

class BeneficioEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = BeneficioEmpleado.objects.all()
    serializer_class = BeneficioEmpleadoSerializer
