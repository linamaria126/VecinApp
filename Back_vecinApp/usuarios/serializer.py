from rest_framework import serializers
from .models import User
from datetime import date

class UserSerializer(serializers.ModelSerializer):

    edad = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = '__all__'  # You can specify fields like ['id', 'username', 'email'] if needed
        read_only_fields = ['id', 'created_at', 'updated_at']  # Campos de solo lectura

    def get_edad(self, obj):
        today = date.today()
        return today.year - obj.fecha_nacimiento.year - ((today.month, today.day) < (obj.fecha_nacimiento.month, obj.fecha_nacimiento.day))
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está registrado.")
        return value
    
    def validate_telefono(self, value):
        """Valida que el campo teléfono no contenga letras."""
        if not value.isdigit():
            raise serializers.ValidationError("El campo teléfono solo puede contener números.")
        return value
    
    def validate_last_name(self, value):
        """Valida que el campo last_name no contenga números."""
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("El campo last_name no puede contener números.")
        return value
    
    def validate_first_name(self, value):
        """Valida que el campo first_name no contenga números."""
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("El campo first_name no puede contener números.")
        return value