from django.db import models
from .unidades import Unidad
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from .divisiones import Division

# Create your models here.
class Unidad_habit(models.Model):

    """Modelo que representa una unidad habitacional dentro de una unidad residencial.
    El ID se genera automáticamente combinando el piso, número y la división (ej: 401A).
    """
    ESTADO_CHOICES = [
        ('OCUPADO', 'Ocupado'),
        ('DISPONIBLE', 'Disponible'),
        ('MANTENIMIENTO', 'En Mantenimiento'),
    ]


    # validadores personalizados
    piso_validator = RegexValidator(
        regex=r'^[0-9]{1,2}$',
        message='El piso debe ser un número de 1 o 2 dígitos (ej: 1, 2, ..., 10, 11, ..., 20).'     
    )


    numero_validator = RegexValidator(
        regex=r'^[0-9]{1,3}[A-Z]?$',
        message='El número debe ser numérico (ej: 01, 02) o alfanumérico (ej: 01A, 02B)'
    )


    id              = models.CharField(max_length=20, 
                                       primary_key=True, 
                                       editable=False, 
                                       help_text="ID generado automáticamente como Piso+Número+División (ej: 401A)")
    
    
    piso            = models.CharField(max_length=2,
                                       validators=[piso_validator],
                                       blank=True, 
                                       null=True,
                                       verbose_name='Piso',
                                       help_text='Número del piso donde se encuentra la unidad habitacional (ej: 1, 2, 3)')   

    estado = models.CharField(max_length=15,
                              choices=ESTADO_CHOICES,
                              default='DISPONIBLE',
                              verbose_name='Estado de la Unidad Habitacional',
                              help_text='Estado actual de la unidad habitacional')

    numero          = models.CharField(max_length=2,
                                       validators=[numero_validator],
                                       verbose_name='Número de Unidad',
                                       help_text='Número de la unidad dentro del piso (ej: 01, 02, 03, 101A)')
    
    cant_habitantes = models.PositiveIntegerField(blank=True,
                                                  null=True,
                                                  validators=[MinValueValidator(1), MaxValueValidator(8)],
                                                  verbose_name='Cantidad de habitantes',
                                                  help_text='Número total de personas que residen en esta unidad habitacional')
    
    
    unidad  = models.ForeignKey(Unidad,on_delete=models.CASCADE,
                                        null=True,
                                        related_name='unidades_habitacionales',
                                        verbose_name='Unidad Residencial',
                                        help_text='Unidad residencial a la que pertenece esta unidad habitacional.')
    
    division        = models.ForeignKey(Division, 
                                        on_delete=models.CASCADE,
                                        null=True,
                                        verbose_name='División',
                                        related_name='unidades_habitacionales',
                                        help_text='División (ej: Torre, Edificio) dentro de la unidad residencial donde se encuentra esta unidad habitacional.')
    
    created_at      = models.DateTimeField(auto_now_add=True,
                                           verbose_name='Fecha de creación')
    updated_at      = models.DateTimeField(auto_now=True, 
                                           null=True,
                                           verbose_name='Última actualización')
    
    is_active       = models.BooleanField(default=True)

    deleted_at        = models.DateTimeField(null=True, 
                                           blank=True,
                                           verbose_name='Fecha de eliminación',
                                           help_text='Fecha y hora en que el registro fue eliminado')

    class Meta:
        db_table = 'unidades_habitacionales'
        verbose_name = 'Unidad Habitacional'
        verbose_name_plural = 'Unidades Habitacionales'
        ordering = ['unidad', 'id']
        constraints = [
            models.UniqueConstraint(
                fields=['unidad', 'piso', 'numero', 'division'],
                name='unique_unidad_habitacional_por_unidad',
                violation_error_message='Ya existe una unidad habitacional con este piso, número y división en la unidad residencial.'
            )
        ]


    def save(self, *args, **kwargs):
        if not self.id:
            piso = self.piso if self.piso else '00'
            numero = self.numero if self.numero else '00'
            division = self.division.id if self.division else 'X'
            self.id = f"{piso}{numero}-{division}"
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return str(self.id)