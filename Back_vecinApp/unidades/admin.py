from django.contrib import admin
from .models.unidades import Unidad
from .models.divisiones import Division
from .models.unidades_habit import Unidad_habit




admin.site.register(Unidad)
admin.site.register(Unidad_habit)
admin.site.register(Division)




# Register your models here




