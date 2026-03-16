from django.db import models
from unidades.models.unidades import TimeStampedModel
from unidades.models.unidades_habit import Unidad_habit

# Create your models here.

class Mascota(TimeStampedModel):


    TIPO_MASC_CHOICES = (
        ('P', 'Perro'),
        ('G', 'Gato'),
    )

    TAMAÑO_CHOICES = (
        ('CH', 'Chico'),
        ('MD', 'Mediano'),
        ('GR', 'Grande'),
    )

     # Campos de la mascota


    tipo_mascota =models.CharField(max_length=4, choices=TIPO_MASC_CHOICES)
    raza = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    tamaño = models.CharField(max_length=50, choices=TAMAÑO_CHOICES, null=True, blank=True)
    
    foto = models.ImageField(
        upload_to='mascotas/',
        blank=True,
        null=True,
        verbose_name='Foto',
        help_text='Foto de la mascota'
    )
    unidad_habit = models.ForeignKey(Unidad_habit, on_delete=models.CASCADE, null=True, related_name='mascotas')
    

    class Meta:
        db_table = 'mascotas'
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        ordering = ['unidad_habit', 'tipo_mascota', 'nombre']

    def __str__(self):
        return f"{self.nombre} - {self.get_tipo_mascota_display()}"
