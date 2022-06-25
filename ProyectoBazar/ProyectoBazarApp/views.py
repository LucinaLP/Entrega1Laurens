from django.shortcuts import render
from .models import Articulo


def index(request):
    articulos=Articulo.objects.all()
    contexto={'articulos': articulos}
    return render(request,"ProyectoBazarApp/index.html")