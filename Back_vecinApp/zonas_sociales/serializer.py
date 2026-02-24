from rest_framework import serializers
from .models import Zona_social

class ZonaSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona_social
        fields = '__all__'