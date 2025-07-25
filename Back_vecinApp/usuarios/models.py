from django.db import models
from django.contrib.auth.models import AbstractUser
from unidades.models.unidades import Unidad
from unidades.models.unidades_habit import Unidad_habit

# Create your models here.

class Documento(models.Model):

     TIPO_DCTO_CHOICES = (
        ('CC', 'Cédula ciudadanía'),
        ('CE', 'Cédula extranjería'),
        ('P', 'Pasaporte'),
        ('PT', 'Permiso de trabajo'),
        ('O', 'Otro'),
    )
     numero_dcto = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='Número de documento')
     tipo_dcto   = models.CharField(max_length=4, choices=TIPO_DCTO_CHOICES)
     delete      = models.BooleanField(default=False)

     
        


     def __str__(self):
          return f'{self.tipo_dcto} {self.numero_dcto}'

class User(AbstractUser):
    
    TIPO_USER = (
        ('A', 'administrador'),
        ('I', 'inquilino'),
        ('P', 'proprietario'),
    )
    email           = models.EmailField(unique=True)
    tipo_user       = models.CharField(max_length=45, choices=TIPO_USER, null=False, default='A')
    telefono        = models.CharField(max_length=45, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now=True)
    update_at       = models.DateTimeField(auto_now=True)
    deleted_at      = models.DateTimeField(auto_now=True, null=True, blank=True)
    unidad          = models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True )
    unidad_habit    = models.ForeignKey(Unidad_habit, on_delete=models.SET_NULL, null=True)
    documento       = models.ForeignKey(Documento, on_delete=models.PROTECT, null=True)
    delete          = models.BooleanField(default=False)


    #comentar en caso de requerir crear más superusuarios
    #Las siguientes dos líneas son para que se emplee email y password para iniciar sesion (y no username)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'