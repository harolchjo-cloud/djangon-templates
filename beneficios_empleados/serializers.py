from rest_framework import serializers
from .models import BeneficioEmpleado

class BeneficioEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficioEmpleado
        fields = '__all__'