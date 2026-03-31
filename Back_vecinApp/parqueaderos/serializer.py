from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import Parqueadero



class ParqueaderoSerializer(serializers.ModelSerializer):
    vehiculo_asignado = serializers.SerializerMethodField()  # Campo personalizado para mostrar el
    
      
    class Meta:
        model = Parqueadero
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']  # Campos de solo lectura

    def validate_numero(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("El número del parqueadero debe contener solo dígitos.")
        if len(value) > 3:
            raise serializers.ValidationError("El número del parqueadero no puede tener más de 3 dígitos.")
        
        if self.instance:
            if Parqueadero.objects.filter(numero=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("El número del parqueadero ya existe.")
        else:
            if Parqueadero.objects.filter(numero=value).exists():
                raise serializers.ValidationError("El número del parqueadero ya existe.")
        return value
    
    @extend_schema_field({
        'type': 'object',
        'properties': {
            'placa': {'type': 'string'},
            'marca': {'type': 'string'},
            'tipo': {'type': 'string'},
            'color': {'type': 'string'},
        },
        'nullable': True
    })

    def get_vehiculo_asignado(self, obj):
            # Usar el related_name 'vehiculos' definido en el modelo Vehiculo
            # Busca el primer vehículo asignado a este parqueadero
            vehiculo = obj.vehiculos.first()  # related_name='vehiculos'
            
            if vehiculo:
                return {
                    'placa': vehiculo.placa,
                    'marca': vehiculo.marca,
                    'tipo': vehiculo.tipo,
                    'color': vehiculo.color
                }
            return None
       
        
       



     