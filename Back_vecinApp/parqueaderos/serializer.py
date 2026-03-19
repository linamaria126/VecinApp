from rest_framework import serializers
from .models import Parqueadero



class ParqueaderoSerializer(serializers.ModelSerializer):
    vehiculo_asignado = serializers.SerializerMethodField()

    class Meta:
        model = Parqueadero
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']  # Campos de solo lectura

     