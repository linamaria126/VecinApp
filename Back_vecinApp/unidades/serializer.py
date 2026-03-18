from webbrowser import get
from rest_framework import serializers
from .models import Unidad, Division, Unidad_habit
import re

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']  # Campos de solo lectura

    def validate_nit(self, value):
        value = value.strip().replace(' ', '')  # Eliminar espacios en blanco al inicio y al final
        patron_con_guion = r'^\d{8,10}-\d$'  # NIT con guion (ej: 123456789-0)
        patron_sin_guion = r'^\d{9,11}$'  # NIT sin guion (ej: 1234567890 o 12345678901)

        if re.match(patron_con_guion, value):
                nit_normalizado = value
        elif re.match(patron_sin_guion, value):
                nit_normalizado = f"{value[:-1]}-{value[-1]}"  # Agregar guion antes del dígito de verificación
        else:
                raise serializers.ValidationError("El NIT debe tener el formato: 123456789-0 (8-10 dígitos, guión, dígito de verificación) o 1234567890 (9-11 dígitos sin guion)")      
        

        if Unidad.objects.filter(nit=value).exists():
            raise serializers.ValidationError("El campo 'nit' debe ser único. Ya existe una unidad con este nit.")
        
        return nit_normalizado


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']  # Campos de solo lectura

class Unidad_habitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad_habit
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']  # Campos de solo lectura

        def validate(self, data):
            """Validar que no existan unidades habitacionales con el mismo número dentro de la misma unidad residencial."""
            piso = data.get('piso')
            numero = data.get('numero')
            division = data.get('division')
            unidad = data.get('unidad')

            if Unidad_habit.objects.filter(piso=piso, numero=numero, division=division, unidad=unidad).exists():
                raise serializers.ValidationError("Ya existe una unidad habitacional con el mismo número en el mismo piso, división y unidad residencial.")
            return data