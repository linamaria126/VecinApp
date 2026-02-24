from django.db import models
from unidades.models.unidades_habit import Unidad_habit
from django.core.validators import RegexValidator

# Create your models here.
class Parqueadero(models.Model):

    numero_validador = RegexValidator(
        regex=r'^[0-9]{1,5}$',
        message='El número del parqueadero debe contener entre 1 y 5 dígitos.'
    )

    numero = models.CharField(max_length=5, validators=[numero_validador], unique=True, primary_key=True)
    unidad_habit= models.ForeignKey(Unidad_habit, on_delete=models.SET_NULL, null=True, related_name='parqueaderos')
    created_at  = models.DateTimeField(auto_now_add=True, null=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True)
    is_active    = models.BooleanField(default=True)
    deleted_at  = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de eliminación')

    class Meta:
        db_table = 'parqueaderos_parqueadero'
        verbose_name = 'Parqueadero'
        verbose_name_plural = 'Parqueaderos'
        ordering = ['unidad_habit', 'numero']
        constraints = [
            models.UniqueConstraint(
                fields=['numero', 'unidad_habit'], 
                name='unique_numero_unidad_habit',
                violation_error_message='El número de parqueadero ya existe en esta unidad habitacional.'
            ),
        ]
