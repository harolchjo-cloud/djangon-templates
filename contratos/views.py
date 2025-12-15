from rest_framework.viewsets import ModelViewSet
from .models import Contrato
from .serializers import ContratoSerializer

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer