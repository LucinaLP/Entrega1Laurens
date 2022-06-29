from unicodedata import name
from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    
    path('nosotros/',nosotros,name="nosotros"),
    path('servicios/',servicios,name="servicios"),
    path('crear_articulo/',crear_articulo,name="crear_articulo"),
    path('buscar_articulo/',buscar_articulo,name="buscar_articulo"),
    ]