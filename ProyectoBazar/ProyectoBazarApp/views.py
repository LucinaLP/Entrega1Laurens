from django.shortcuts import redirect, render
from .models import *


def inicio(request):
    articulos = Articulo.objects.all()
    contexto = {'articulos': articulos}
    return render(request,"ProyectoBazarApp/index.html",contexto)

def crear_articulo(request):    
    
    if request.method == "POST":
        
        info_formulario = request.POST
        
        articulo = Articulo(producto=info_formulario["producto"], cantidad=int(info_formulario["cantidad"]), precio=float(info_formulario["precio"]))
        
        articulo.save()
        
        return redirect("inicio")
        
    else:
        return render(request,"ProyectoBazarApp/formulario_articulo.html",{})

def base(request):
    
    return render(request,"ProyectoBazarApp/base.html",{})

def nosotros(request):
    info = Nosotros.objects.all()
    contexto = {'info': info}
    return render(request,"ProyectoBazarApp/nosotros.html",contexto)

def servicios(request):
    servicios = Servicios.objects.all()
    contexto = {'servicios': servicios}
    return render(request,"ProyectoBazarApp/servicios.html",contexto)