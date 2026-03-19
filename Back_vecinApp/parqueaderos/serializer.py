from rest_framework import serializers
from .models import Parqueadero



class ParqueaderoSerializer(serializers.ModelSerializer):
    vehiculo_asignado = serializers.SerializerMethodField()

    class Meta:
        model = Parqueadero
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']  # Campos de solo lectura

        def validate_numero(self, value):
            if not value.isdigit():
                raise serializers.ValidationError("El número del parqueadero debe contener solo dígitos.")
            if len(value) > 3:
                raise serializers.ValidationError("El número del parqueadero no puede tener más de 3 dígitos.")
            if Parqueadero.objects.filter(numero=value).exists():
                raise serializers.ValidationError("El número del parqueadero ya existe.")   
            return value



     