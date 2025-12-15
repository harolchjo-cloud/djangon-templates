from rest_framework.viewsets import ModelViewSet
from .models import Nomina
from .serializers import NominaSerializer

class NominaViewSet(ModelViewSet):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializer