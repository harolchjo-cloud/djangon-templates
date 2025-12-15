from rest_framework.viewsets import ModelViewSet
from .models import Puesto
from .serializers import PuestoSerializer

class PuestoViewSet(ModelViewSet):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer