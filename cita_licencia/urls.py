from django.urls import path
from . import viewsr

from .views.cliente import tokenCliente
from .views.cliente import actualizaCliente
from .views.cliente import validaTokenCliente

from .views.calendario import cargaDiasMes
from .views.calendario import getHorariosLibres

urlpatterns = [
    path("allClientes",viewsr.getClientes),

    #Cliente
    path("cliente/tokenCliente",tokenCliente),
    path("cliente/validaTokenCliente",validaTokenCliente),
    path("cliente/actualizaCliente",actualizaCliente),
    
    #Calendario
    path("calendario/cargaDiasMes",cargaDiasMes),
    path("calendario/horariosLibres",getHorariosLibres)
    
    
]