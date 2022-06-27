from unicodedata import name
from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio),
    
    path('nosotros/',nosotros),
    path('servicios/',servicios),
    path('base/',base),
]