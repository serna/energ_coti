from django.contrib import admin
from .models import Residencial
from .models import Inversor, Proovedor,Instalacion,Configuracion,Configuracion2
admin.site.register(Residencial)
admin.site.register(Inversor)
admin.site.register(Proovedor)
admin.site.register(Instalacion)
admin.site.register(Configuracion)
admin.site.register(Configuracion2)