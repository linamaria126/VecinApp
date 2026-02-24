from django.db import models
from django.core.validators import  RegexValidator



# Create your models here.
class Unidad(models.Model):
   
    UNIDAD_HABITACIONAL_CHOICES = (
        ('A', 'Apartamento'),
        ('C', 'Casa'),
        ('M', 'Mixto (Apartamentos y Casas)'),
        ('O', 'Otro'),
    )



    # Validaciones personalizadas
    nit_validator = RegexValidator(
        regex=r'^[0-9]{9}-[0-9]$',
        message='El NIT debe tener el formato: 123456789-0'
    )

    telefono_validator = RegexValidator(
        regex=r'^\+?[0-9]{7,15}$',
        message='El teléfono debe tener entre 7 y 15 dígitos. Puede incluir + al inicio.'
    )
    
    nombre     = models.CharField(max_length=100, 
                                  unique=True, 
                                  verbose_name='Nombre de la unidad Residencial',
                                  help_text='Nombre oficial de la unidad residencial (ej: Conjunto Residencial Capriani)')

    nit        = models.CharField(max_length=20, 
                                  validators=[nit_validator], 
                                  unique=True, 
                                  verbose_name='NIT')
    
    direccion  = models.CharField(max_length=200, 
                                  verbose_name='Dirección completa', 
                                  help_text='Dirección completa incluyendo ciudad y barrio')
    
    email      = models.EmailField(max_length=254, 
                                   unique=True,
                                   null=True,
                                   blank=True,
                                   verbose_name='Correo electrónico de contacto',
                                   help_text='Correo electrónico de contacto de la administración.')
    
    telefono   = models.CharField(max_length=45, 
                                  validators=[telefono_validator],
                                  verbose_name='Teléfono de contacto',
                                  help_text='Teléfono principal de contacto  de la administración.')
    
    tipo_unidad_habit   = models.CharField(max_length=1, 
                                           choices=UNIDAD_HABITACIONAL_CHOICES,
                                           verbose_name='Tipo de Unidades Habitacionales',
                                           help_text='Tipo predominante de viviendas en la unidad residencial')    

    cantidad_unid_habit = models.IntegerField(blank=True, null=True)

    link_registro       = models.URLField(max_length=300, 
                                          blank=True, 
                                          null=True, 
                                          help_text='Enlace para el registro de nuevos usuarios.')
    
    logo                = models.ImageField(upload_to='logos/', 
                                            max_length=200, 
                                            null=True, 
                                            blank=True, 
                                            help_text='Logo de la unidad residencial.')
    
    created_at  = models.DateTimeField(auto_now_add=True, 
                                       verbose_name='Fecha de creación')
    
    updated_at  = models.DateTimeField(auto_now=True, 
                                       null=True, 
                                       verbose_name='Última actualización')
    
    is_active   = models.BooleanField(default=True)
    
    deleted_at        = models.DateTimeField(null=True, 
                                           blank=True,
                                           verbose_name='Fecha de eliminación',
                                           help_text='Fecha y hora en que el registro fue eliminado')

    
    
  

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'unidades_residenciales'
        verbose_name = 'Unidad_Residencial'
        verbose_name_plural = 'Unidades Residenciales'
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['nombre']),
            models.Index(fields=['nit']),
            models.Index(fields=['is_active']),
        ]

    def soft_delete(self):
        """Método para eliminación lógica"""
        self.is_active = False
        # self.deleted_at = timezone.now()  # Si usas deleted_at
        self.save()

    def activate(self):
        """Método para reactivar la unidad"""
        self.is_active = True
        # self.deleted_at = None  # Si usas deleted_at
        self.save()