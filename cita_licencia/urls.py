from django.urls import path
from . import views
urlpatterns = [
    path("allClientes",views.getClientes)
]