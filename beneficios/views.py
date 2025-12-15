from rest_framework import viewsets
from .models import Beneficio
from .serializers import BeneficioSerializer

class BeneficioViewSet(viewsets.ModelViewSet):
    queryset = Beneficio.objects.all()
    serializer_class = BeneficioSerializer