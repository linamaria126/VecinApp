from django.utils import timezone
from rest_framework import serializers
from .models import Reserva
from django.contrib.auth import get_user_model


User = get_user_model()



class ReservaSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.SerializerMethodField()
    zona_social_nombre = serializers.SerializerMethodField()
    duracion_horas = serializers.SerializerMethodField()
    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ['fecha_reserva', 'estado']

    def get_usuario_nombre(self, obj):
        if obj.usuario:
            return obj.usuario.get_full_name() or obj.usuario.email
        return "Usuario Eliminado"
    
    def get_zona_social_nombre(self, obj):
        return obj.zona_social.nombre if obj.zona_social else None
    
    def get_duracion_horas(self, obj):
        if obj.fin_reserva and obj.inicio_reserva:
            duracion = obj.fin_reserva - obj.inicio_reserva
            return duracion.total_seconds() / 3600  # Convertir a horas
        return None
    
    def validate(self, data):
        """Validaciones cruzadas de reserva """
        inicio = data.get('inicio_reserva')
        fin = data.get('fin_reserva')
        zona_social = data.get('zona_social')
        if inicio and fin and inicio >= fin:
            raise serializers.ValidationError("La fecha de inicio debe ser anterior a la fecha de fin.")
        if inicio <= timezone.now():
            raise serializers.ValidationError("La fecha de inicio debe ser en el futuro.")
        if zona_social:
            conflictos = Reserva.objects.filter(
                zona_social=zona_social,
                estado=['A', 'P'],  # Solo considerar reservas aprobadas o pendientes
                inicio_reserva__lt=fin,
                fin_reserva__gt=inicio
            )
            if self.instance:
                conflictos = conflictos.exclude(id=self.instance.id)
            if conflictos.exists():
                raise serializers.ValidationError("La zona social ya está reservada en el período seleccionado.")
        return data


