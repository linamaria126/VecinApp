from django.db import models
from django.conf import settings
from unidades.models.unidades import TimeStampedModel

# Create your models here.
class Publicacion(TimeStampedModel):
    TIPO_PUBLICACION_CHOICES = [
        ('venta', '🛒 Venta'),
        ('servicio', '🔧 Servicio'),
        ('busqueda', '🔍 Búsqueda'),
        ('donacion', '🎁 Donación'),
        ('intercambio', '🔄 Intercambio'),
        ('evento', '📅 Evento'),
        ('recomendacion', '⭐ Recomendación'),
        ('otro', 'Otro'),
    ]

    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('vendido', 'Vendido'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
        ('oculto', 'Oculto'),
    ]


    titulo = models.CharField(max_length=200, verbose_name='Título')
    contenido = models.TextField(verbose_name='Contenido')
    tipo_publicacion = models.CharField(max_length=20, choices=TIPO_PUBLICACION_CHOICES, default='otro')
    estado = models.CharField(max_length=12,choices=ESTADO_CHOICES,default='activo', verbose_name='Estado')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='publicaciones')
    imagen = models.ImageField(upload_to='publicaciones/', max_length=200, null=True, blank=True)
    telefono_informes = models.CharField(max_length=15,blank=True, null=True, help_text='Número de Teléfono para solicitar información adicional')
    email_informes = models.EmailField(blank=True, null=True, help_text='Email de para solicitar información adicional')
    whatsapp_informes = models.CharField(max_length=15, blank=True, null=True, help_text='Número de WhatsApp para solicitar información adicional')
    

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-fecha_publicacion']

        permissions = [
            ('can_feature_post', 'Puede destacar publicaciones'),
            ('can_moderate_post', 'Puede moderar publicaciones'),
        ]



    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.tipo_publicacion} - {self.estado}"