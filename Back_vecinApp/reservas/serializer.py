from rest_framework import serializers
from .models import Reserva



class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ['fecha_reserva', 'estado']

