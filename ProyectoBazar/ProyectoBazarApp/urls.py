from unicodedata import name
from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('login', login_request, name="login"),
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    path('editar_perfil', editar_perfil, name="editar_perfil"),
    path('agregar_avatar', agregar_avatar, name="agregar_avatar"),
    
    path('nosotros/',nosotros,name="nosotros"),
    path('servicios/',servicios,name="servicios"),
    path('crear_articulo/',crear_articulo,name="crear_articulo"),
    path('eliminar_articulo/<articulo_id>',eliminar_articulo,name="eliminar_articulo"),
    path('editar_articulo/<articulo_id>',editar_articulo,name="editar_articulo"),
    path('buscar_articulo/',buscar_articulo,name="buscar_articulo"),
    path('crear_servicio/',crear_servicio,name="crear_servicio"),
    path('eliminar_servicio/<servicio_id>',eliminar_servicio,name="eliminar_servicio"),
        
    ]