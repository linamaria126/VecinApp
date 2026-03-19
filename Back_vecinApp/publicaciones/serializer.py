from rest_framework import serializers
from .models import Publicacion
from django.contrib.auth.models import get_user_model


User = get_user_model()

class PublicacionSerializer(serializers.ModelSerializer):

    autor_nombre = serializers.SerializerMethodField()
    tiempo_publicacion = serializers.SerializerMethodField()
    class Meta:
        model = Publicacion
        fields = '__all__'
        read_only_fields = ['fecha_publicacion', 'autor']  # Solo lectura para estos campos

    def get_autor_nombre(self, obj):
        if obj.autor:
            return obj.autor.get_full_name() or obj.autor.email
        return "Usuario Eliminado"

    def validate_titulo(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El título debe tener al menos 5 caracteres.")
        if len(value) > 100:
            raise serializers.ValidationError("El título no puede tener más de 100 caracteres.")
        return value
    
    def validate_contenido(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("El contenido debe tener al menos 20 caracteres.")
        return value
    
    def validate_whatsapp(self, value):
        """ Validar el número de WhatsApp, si lo proporciona. """
        if len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError("El número de WhatsApp debe tener entre 10 y 15 caracteres.")
        if value and not value.isdigit():
            raise serializers.ValidationError("El número de WhatsApp debe contener solo dígitos.")  
        return value
    
    def get_tiempo_publicacion(self, obj):
        from django.utils.timesince import timesince
        return timesince(obj.fecha_publicacion) + " atrás"
    
    
    
    class PublicacionFilterSerializer(serializers.Serializer):
        titulo = serializers.CharField(required=False, max_length=100)
        estado = serializers.ChoiceField(required=False, choices=Publicacion.ESTADO_CHOICES)
        autor = serializers.CharField(required=False, max_length=100)
        fecha_publicacion = serializers.DateField(required=False)
        tipo_publicacion = serializers.ChoiceField(required=False, choices=Publicacion.TIPO_PUBLICACION_CHOICES)
        