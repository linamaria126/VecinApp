from rest_framework import serializers
from .models import Unidad, Division, Unidad_habit

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class Unidad_habitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad_habit
        fields = '__all__'