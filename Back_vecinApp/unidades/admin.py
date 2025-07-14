from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models.user import User
from .models.unidades import Unidad
from .models.divisiones import Division

admin.site.register(User)

admin.site.register(Unidad)

admin.site.register(Division)

# Register your models here.
class UserAdmin(BaseUserAdmin):
    pass



