from rest_framework import viewsets
from .models import BeneficioEmpleado
from .serializers import BeneficioEmpleadoSerializer

class BeneficioEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = BeneficioEmpleado.objects.all()
    serializer_class = BeneficioEmpleadoSerializer