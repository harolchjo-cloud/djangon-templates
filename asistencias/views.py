from rest_framework.viewsets import ModelViewSet
from .models import Asistencia
from .serializers import AsistenciaSerializer

class AsistenciaViewSet(ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer