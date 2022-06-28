from django.contrib import admin

from .models import *

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('producto', 'detalle', 'cantidad', 'color', 'precio')

admin.site.register(Articulo, ArticuloAdmin)

class NosotrosAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'email', 'instagram')
    
admin.site.register(Nosotros, NosotrosAdmin)

class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Servicios, ServiciosAdmin)