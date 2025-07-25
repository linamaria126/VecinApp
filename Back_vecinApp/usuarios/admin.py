from django.contrib import admin
from .models import User
from .models import Documento

# Register your models here.
admin.site.register(User)
admin.site.register(Documento)

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['numero_dcto', 'tipo_dcto']
