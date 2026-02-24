from django.db import models
from django.core.validators import RegexValidator
from unidades.models import Unidad_habit
from parqueaderos.models import Parqueadero



# Create your models here.
class Vehiculo(models.Model):
              
        

        TIPO_VEHICULO_CHOICES = (
        ('CARRO', 'Carro'),
        ('MOTO', 'Moto'),
        ('CAMIONETA', 'Camioneta'),
        ('OTRO', 'Otro'),

        )

        # Validadores

        placa_validador = RegexValidator(
                regex=r'^[A-Z]{3}[0-9]{3}$|^[A-Z]{3}[0-9]{2}[A-Z]$|^[A-Z]{2}[0-9]{4}$',
                message='Formato de placa inválido. Use: ABC123, ABC12D o AB1234'
        )

        placa       = models.CharField(max_length=10, 
                                       primary_key=True, 
                                       validators=[placa_validador],
                                       help_text='Formato: ABC123, ABC12D o AB1234')
        
        tipo        = models.CharField(max_length=10, 
                                       choices=TIPO_VEHICULO_CHOICES, 
                                       default='CARRO', 
                                       verbose_name='Tipo de Vehículo')

        marca       = models.CharField(max_length=50, null=True, blank=True)
        color       = models.CharField(max_length=50, null=True, blank=True)
        unidad_habit    = models.ForeignKey(Unidad_habit, on_delete=models.SET_NULL, null=True, related_name='vehiculos')
        parqueadero_id  = models.ForeignKey(Parqueadero, on_delete=models.SET_NULL, null=True, related_name='vehiculos', blank=True)
        created_at  = models.DateTimeField(auto_now_add=True)
        updated_at  = models.DateTimeField(auto_now=True, null=True)
        deleted_at      = models.DateTimeField(null=True, blank=True,
                                           verbose_name='Fecha de eliminación',
                                           help_text='Fecha y hora en que el registro fue eliminado')




        def __str__(self):
                return f"{self.placa} - {self.tipo} - {self.unidad_habit}"
        

        class Meta:
                db_table = 'vehiculos_vehiculo'
                verbose_name = 'Vehículo'
                verbose_name_plural = 'Vehículos'
                ordering = ['unidad_habit', 'placa']
                unique_together = ('placa', 'unidad_habit')

        @property
        def informacion_completa(self):
                """Verifica si el vehículo tiene información completa"""
                campos_requeridos = [
                self.placa,
                self.marca,
                self.color,
                self.tipo,
                self.unidad_habit
                ]
                return all(campos_requeridos)
        
        @property
        def tiene_parqueadero_asignado(self):
            """Verifica si el vehículo tiene parqueadero asignado"""
            return self.parqueadero_id is not None