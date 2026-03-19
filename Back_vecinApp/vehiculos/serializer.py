from rest_framework import serializers
from .models import Vehiculo
from parqueaderos.models import Parqueadero

class VehiculoSerializer(serializers.ModelSerializer):
    parqueadero_info = serializers.SerializerMethodField()

    class Meta:
        model = Vehiculo
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

  