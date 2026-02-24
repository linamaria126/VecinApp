from django.db import models
from .unidades import Unidad
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError



# Create your models here.
class Division(models.Model):

    TIPO_DIVISION_CHOICES = [
        ('TORRE', 'Torre'),
        ('EDIFICIO', 'Edificio'),
        ('MANZANA', 'Manzana'),
        ('BLOQUE', 'Bloque'),
        ('ETAPA', 'Etapa'),
        ('SECTOR', 'Sector'),
        ('ZONA', 'Zona'),
        ('LOTE', 'Lote'),
    ]

   
    unidad = models.ForeignKey(
        Unidad, 
        on_delete=models.CASCADE,
        null=True,
        related_name='divisiones',
        verbose_name='Unidad Residencial',
        help_text='Unidad residencial a la que pertenece esta división.'
    )

    tipo_division = models.CharField(
        max_length=20,
        choices=TIPO_DIVISION_CHOICES,
        default='TORRE',
        verbose_name='Tipo de División',
        help_text='Tipo de agrupación arquitectónica (ej: Torre, Edificio, Manzana). Mantenga consistencia en la nomenclatura para todo el conjunto residencial.'
    )

    identificador = models.CharField(
        max_length=10,
        verbose_name='Identificador único',
        help_text='Letra/numero que identifica la división (ej: 1, 2, A, B, ). Mantenga consistencia en la nomenclatura para todo el conjunto residencial.',
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]+$',
                message='Solo se permiten caracteres alfanuméricos (letras y números).'
            )
        ],
        default='1',
    )

    nombre = models.CharField(
        max_length=100,
        editable=False, # No editable para evitar cambios manuales
        verbose_name='Nombre completo de la División',
        default='',
        help_text='Nombre o número de la división dentro de la unidad (ej: Torre A, Edificio 1, Manzana B). Mantenga consistencia en la nomenclatura para todo el conjunto residencial.'
    )

    cantidad_pisos = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Cantidad de Pisos',
        validators=[MinValueValidator(1), MaxValueValidator(150)],
        help_text='Cantidad de pisos que tiene la división. Obligatorio para Torres y Edificios.'
    )

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
        db_table = 'divisiones'
        verbose_name = 'Division'
        verbose_name_plural = 'Divisiones'
        ordering = ['unidad', 'nombre']
        
        constraints = [
            models.UniqueConstraint(
                fields=['unidad', 'nombre'],
                name='unique_nombre_por_unidad'
            )
        ]

    def __str__(self):
        return self.nombre
    

    #Validaciones:

    def clean(self):
        # 1. Ejecuta validaciones básicas de Django
        super().clean()  # Valida tipos de datos, max_length, etc.  

        # 2. Validaciones personalizadas
        if not self.identificador.isalnum():
            raise ValidationError({'identificador': 'Solo se permiten letras y números sin espacios'})
        
        # Validar coherencia para torres/edificios
        if self.tipo_division in ['TORRE', 'EDIFICIO'] and not self.cantidad_pisos:
            raise ValidationError({'cantidad_pisos': 'Debe especificar la cantidad de pisos para torres o edificios.'})
        
        
    def save(self, *args, **kwargs):
            
        #Construir nombre: "Tipo + Identificador"(ej: Torre A)
        self.nombre = f"{self.get_tipo_division_display()} {self.identificador}"

        self.full_clean()  # Ejecuta validaciones personalizadas

        # Llama al método save de la clase padre
        super().save(*args, **kwargs)

    
    @property
    def cantidad_unidades_habitacionales(self):
        return self.unidades_habitacionales.count()
    
    @property
    def nombre_corto(self):
        """Versión compacta del nombre (ej: 'T-1')"""
        return f"{self.tipo_division[0]}-{self.identificador}"
    
   
        
