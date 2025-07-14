from django.db import models
from .unidades import Unidad
from .unidades_habit import Unidad_habit
from . documentos import Documento
from django.contrib.auth.models import AbstractUser

# Create your models here.
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
    unidad          = models.ForeignKey(Unidad, on_delete=models.PROTECT, null=True )
    unidad_habit    = models.ForeignKey(Unidad_habit, on_delete=models.PROTECT, null=True)
    documento       = models.ForeignKey(Documento, on_delete=models.PROTECT, null=True)


    #comentar en caso de requerir crear más superusuarios
    #Las siguientes dos líneas son para que se emplee email y password para iniciar sesion (y no username)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'