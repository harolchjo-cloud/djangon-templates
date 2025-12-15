from rest_framework import serializers
from .models import Vacacion

class VacacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacacion
        fields = '__all__'