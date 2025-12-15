from rest_framework import serializers
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

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = '__all__'


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'


class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'


class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'


class VacacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacacion
        fields = '__all__'


class NominaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomina
        fields = '__all__'


class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'


class BeneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficio
        fields = '__all__'


class BeneficioEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficioEmpleado
        fields = '__all__'
