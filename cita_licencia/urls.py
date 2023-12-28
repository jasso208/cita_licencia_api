from django.urls import path
from . import viewsr

from .views.cliente import tokenCliente
from .views.cliente import tokenClienteWhatsapp
from .views.cliente import actualizaCliente
from .views.cliente import validaTokenCliente
from .views.cliente import validaClienteAdmin

from .views.calendario import cargaDiasMes
from .views.calendario import getHorariosLibres

from .views.cita import generaCita
from .views.cita import getCitas
from .views.cita import consultaCita
from .views.cita import actualizaCita

from .views.cita import getAllCitas
from .views.pais import getAllPais

urlpatterns = [
    path("allClientes",viewsr.getClientes),

    #Cliente
    path("cliente/tokenCliente",tokenCliente),
    path("cliente/tokenClienteWhatsapp",tokenClienteWhatsapp),
    path("cliente/validaTokenCliente",validaTokenCliente),
    path("cliente/actualizaCliente",actualizaCliente),
    path("cliente/validaClienteAdmin",validaClienteAdmin),
    

    
    #Calendario
    path("calendario/cargaDiasMes",cargaDiasMes),
    path("calendario/horariosLibres",getHorariosLibres),

    #cita
    path("cita/generaCita",generaCita),
    path("cita/getCitas",getCitas),
    path("cita/getAllCitas",getAllCitas),
    path("cita/consultaCita",consultaCita),
    path("cita/actualizaCita",actualizaCita),
    

    #Pais
    path("pais/getAllPais",getAllPais)
    
    
    
]