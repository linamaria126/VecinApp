from rest_framework import serializers
from .models import Mascota



class MascotaSerializer(serializers.ModelSerializer):
    unidad_habit_info = serializers.SerializerMethodField()

    class Meta:
        model = Mascota
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']  # Campos de solo lectura

        def get_unidad_habit_info(self, obj):
            return {
                'id': obj.unidad_habit.id,
                'nombre': obj.unidad_habit.nombre,
                'direccion': obj.unidad_habit.direccion
            }