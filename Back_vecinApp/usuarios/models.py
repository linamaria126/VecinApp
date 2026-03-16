from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from unidades.models.unidades import Unidad, TimeStampedModel
from unidades.models.unidades_habit import Unidad_habit

#Create your models here.


class User(AbstractUser, TimeStampedModel):
    #AbstractUser ya incluye: username, password, first_name, last_name, email, is_staff, 
    # is_active, date_joined, last_login
    
    TIPO_USER_CHOICES = (
        ('AD', 'administrador'),
        ('IN', 'inquilino'),
        ('PR', 'propietario-residente'),
        ('PN', 'propietario-no-residente'),
    )

    TIPO_DCTO_CHOICES = (
        ('CC', 'Cédula ciudadanía'),
        ('CE', 'Cédula extranjería'),
        ('PP', 'Pasaporte'),
        ('PT', 'Permiso de trabajo'),
        ('O', 'Otro'),
    )

    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
        ('ND', 'Prefiero no decirlo'),
    )

    # Validadores
    telefono_validator = RegexValidator(
        regex=r'^\+?[0-9]{7,15}$',
        message='El teléfono debe tener entre 7 y 15 dígitos. Puede incluir + al inicio.'
    )

    documento_validator = RegexValidator(
        regex=r'^[0-9a-zA-Z-]{5,20}$',
        message='El documento debe contener entre 5 y 20 caracteres alfanuméricos o guiones.'
    )
    
    #Campos de identificación:
    numero_dcto     = models.CharField(max_length=20, validators=[documento_validator], null=True, unique=True, verbose_name='Número de documento')
    tipo_dcto       = models.CharField(max_length=4, choices=TIPO_DCTO_CHOICES,  default='CC')
    
    #información personal
    genero         = models.CharField(max_length=2, choices=GENERO_CHOICES, null=True, blank=True, verbose_name='Género')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    
    #Información de contacto
    telefono        = models.CharField(max_length=45, validators=[telefono_validator], null=True, blank=True, verbose_name='Teléfono')
    email           = models.EmailField(unique=True)
    
    tipo_user       = models.CharField(max_length=45, choices=TIPO_USER_CHOICES, null=False, default='A')
    unidad_residencial = models.ForeignKey(Unidad, on_delete=models.CASCADE, null=True, related_name='usuarios')
    unidad_habit    = models.ForeignKey(Unidad_habit, on_delete=models.CASCADE, null=True, related_name='residentes')
    
    groups          = models.ManyToManyField('auth.Group', 
                                             related_name='usuario_set', 
                                             blank=True, 
                                             related_query_name='usuario')
    user_permissions = models.ManyToManyField('auth.Permission',
                                              verbose_name='user permissions', 
                                              related_name='usuario_set', 
                                              blank=True)

    #comentar en caso de requerir crear más superusuarios
    #Las siguientes dos líneas son para que se emplee email y password para iniciar sesion (y no username)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        # Si no se proporciona username, usar el email
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['unidad_residencial', 'first_name', 'last_name']
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'numero_dcto'],
                name='unique_documento_por_unidad',
                violation_error_message='Ya existe un usuario con este documento en la unidad residencial.'
            ),
        ]