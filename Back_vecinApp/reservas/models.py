from django.db import models
from usuarios.models import User
from unidades.models import Unidad
from zonas_sociales.models import Zona_social
from unidades.models.unidades_habit import Unidad_habit

# Create your models here.
class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('A', 'Aprobada'),
        ('R', 'Rechazada'),
        ('C', 'Cancelada'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    unidad_residencial = models.ForeignKey(Unidad, on_delete=models.CASCADE, null=True, related_name='reservas')
    zona_social = models.ForeignKey(Zona_social, on_delete=models.CASCADE, null=True, related_name='reservas')
    unidad_habit = models.ForeignKey(Unidad_habit, on_delete=models.CASCADE, null=True, related_name='reservas')
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='P')
    motivo = models.TextField(blank=True, null=True, verbose_name='Motivo de Reserva')
    inicio_reserva = models.DateTimeField(null=True, blank=True)
    fin_reserva = models.DateTimeField(null=True, blank=True)
    numero_personas = models.IntegerField(null=True, blank=True, verbose_name='Número de Personas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True)
    is_delete      = models.BooleanField(default=False)

    class Meta:
        db_table = 'reservas_reserva'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['inicio_reserva']

    def __str__(self):
        return f'Reserva {self.id} : {self.inicio_reserva} - {self.zona_social} - {self.unidad_habit}'