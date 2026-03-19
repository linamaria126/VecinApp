from rest_framework import serializers
from .models import Zona_social
from reservas.models import Reserva
from datetime import datetime

class ZonaSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona_social
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

        def get_disponibilidad(self, obj):
            """Determina la disponibilidad de la zona social en función de las reservas."""
            hoy = datetime.now().date()
            reservas_activas = Reserva.objects.filter(zona_social=obj, fecha_reserva__gte=hoy)
            return not reservas_activas.exists()
        
        def get_proxima_reserva(self, obj):
            """Obtiene la próxima reserva para la zona social."""
            hoy = datetime.now().date()
            proxima_reserva = Reserva.objects.filter(zona_social=obj, fecha_reserva__gte=hoy).order_by('fecha_reserva').first()
            if proxima_reserva:
                return proxima_reserva.fecha_reserva
            return None
        
        