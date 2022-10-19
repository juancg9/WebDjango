from django.contrib import admin

from DataMundial.views import registro
from .models import *
# Register your models here.

admin.site.register(selecciones)
admin.site.register(grupo)
admin.site.register(Registro)
admin.site.register(Avatar)
admin.site.register(Details)