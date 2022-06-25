from django.contrib import admin

from .models import Articulo

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('producto', 'detalle', 'cantidad', 'color', 'precio')

admin.site.register(Articulo, ArticuloAdmin)
