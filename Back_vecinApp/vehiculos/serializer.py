from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import Vehiculo


class VehiculoSerializer(serializers.ModelSerializer):
    parqueadero_info = serializers.SerializerMethodField()


    class Meta:
        model = Vehiculo
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


    @extend_schema_field({
        'type': 'object',
        'properties': {
            
            'numero': {'type': 'string'},
            
        },
        'nullable': True
    })

    def get_parqueadero_info(self, obj):
        if obj.parqueadero_id:
            
            return {
                'numero': obj.parqueadero_id.numero,
            
            }
        return None


  