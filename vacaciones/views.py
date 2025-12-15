from rest_framework.viewsets import ModelViewSet
from .models import Vacacion
from .serializers import VacacionSerializer

class VacacionViewSet(ModelViewSet):
    queryset = Vacacion.objects.all()
    serializer_class = VacacionSerializer