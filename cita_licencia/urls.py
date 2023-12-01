from django.urls import path
from . import viewsr

from .views.cliente import validaCliente
from .views.cliente import actualizaCliente

from .views.calendario import cargaDiasMes

urlpatterns = [
    path("allClientes",viewsr.getClientes),

    #Cliente
    path("cliente/validaCliente",validaCliente),
    path("cliente/actualizaCliente",actualizaCliente),
    
    #Calendario
    path("calendario/cargaDiasMes",cargaDiasMes)
    
]