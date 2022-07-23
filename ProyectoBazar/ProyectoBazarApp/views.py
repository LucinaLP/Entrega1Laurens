from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def inicio(request):
    articulos = Articulo.objects.all()
    contexto = {'articulos': articulos}
    return render(request,"ProyectoBazarApp/index.html",contexto)

def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                login(request, user)
                return redirect('inicio')
            
            else:
                return redirect('login')
            
        else:
            return redirect('login')
        
    form=AuthenticationForm()
    
    return render(request,"ProyectoBazarApp/login.html",{"form":form})

def register_request(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            
            form.save()
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                login(request, user)
                return redirect('inicio')
            
            else:
                return redirect('login')
            
            return redirect("login")
        
        return render(request, "ProyectoBazarApp/register.html", {"form": form})
    
    form = UserRegisterForm()
    
    return render(request, "ProyectoBazarApp/register.html", {"form": form})

def logout_request(request):
    logout(request)
    return redirect("inicio")

@login_required
def editar_perfil(request):    
    user = request.user
    
    if request.method == "POST":
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
                        
            user.save()
            
            return redirect("inicio")
                    
    else:
        form = UserEditForm(initial={'email': user.email, "first_name": user.first_name, "last_name": user.last_name})
    
    return render(request,"ProyectoBazarApp/editar_perfil.html",{"form":form})

@login_required
@staff_member_required
def crear_articulo(request):    
    
    if request.method == "POST":
        
        formulario = NuevoArticulo(request.POST)
        
        if formulario.is_valid():
            
            info_articulo = formulario.cleaned_data    
        
            articulo = Articulo(producto=info_articulo["producto"], cantidad=int(info_articulo["cantidad"]), precio=float(info_articulo["precio"]))
        
            articulo.save()
        
            return redirect("inicio")
        
        else:
        
            return render(request,"ProyectoBazarApp/formulario_articulo.html",{"form":formularioVacio})
        
    else:
        
        formularioVacio = NuevoArticulo()
        
        return render(request,"ProyectoBazarApp/formulario_articulo.html",{"form":formularioVacio})
    
def buscar_articulo(request):
    
    if request.method == "POST":
        
        articulo = request.POST["producto"]
        
        articulos = Articulo.objects.filter(producto__icontains=articulo)
        
        return render(request,"ProyectoBazarApp/busqueda_articulo.html",{"articulos":articulos})
    
    else:        
    
        articulos = []
        
        return render(request,"ProyectoBazarApp/busqueda_articulo.html",{"articulos":articulos})

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