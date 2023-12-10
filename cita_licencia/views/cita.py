from rest_framework.decorators import api_view
from rest_framework.response import Response
from cita_licencia.models.cliente import Cliente
from cita_licencia.models.horario_dia import HorarioDia
from cita_licencia.models.cita import Cita
from cita_licencia.models.estatus_cita import EstatusCita
from django.core.paginator import Paginator


import datetime

"""
    Genera nueva cita.
        Parametros
            id_cliente = request.data["id_cliente"]
            id_horario_cita = request.data["id_horario"]
            nombre = request.data["nombre"]
            apellido_p = request.data["apellido_p"]
            apellido_m = request.data["apellido_m"]
            whatsapp = request.data["whatsapp"]
            email = request.data["email"]
            pais_destino = request.data["pais_destino"]
            fecha_viaje = request.data["fecha_viaje"]

"""
@api_view(["POST"])
def generaCita(request):
    id_cliente = request.data["id_cliente"]
    id_horario_cita = request.data["id_horario_cita"]
    nombre = request.data["nombre"]
    apellido_p = request.data["apellido_p"]
    apellido_m = request.data["apellido_m"]
    whatsapp = request.data["whatsapp"]
    email = request.data["email"]
    pais_destino = request.data["pais_destino"]
    fecha_viaje = request.data["fecha_viaje"]

    try:
        cliente = Cliente.objects.get(id = id_cliente)
    except:
        return Response({"estatus":"0","msj":"Error al generar la cita. Cliente no existe."})

    try:
        hora_cita = HorarioDia.objects.get(id = id_horario_cita,cliente_reserva = None)
    except:
        return Response({"estatus":"0","msj":"Error al generar la cita. Horario no disponible."})
    
    if(cliente.whatsapp != None and cliente.whatsapp != 0):
        if(str(cliente.whatsapp).strip() != whatsapp.strip() or cliente.email.strip() != email.strip()):
            return Response({"estatus":"0","msj":"El email y/o whatsapp no corresponden con el cliente indicado."})
    else:
        if(cliente.email.strip() != email.strip()):
            return Response({"estatus":"0","msj":"El email no corresponden con el cliente indicado."})
    
    
    cita = Cita()
    cita.nombre = nombre
    cita.apellido_p = apellido_p
    cita.apellido_m = apellido_m
    cita.whatsapp = whatsapp
    cita.email = email
    cita.pais_destino = pais_destino
    cita.fecha_viaje = fecha_viaje
    cita.cliente = cliente
    cita.horario_cita = hora_cita
    cita.estatus_cita = EstatusCita.objects.get(id=1)
    cita.save()

    hora_cita.cliente_reserva = cliente
    hora_cita.disponible = 0
    hora_cita.save()

    cita_nueva = Cita.objects.filter(id = cita.id).values("nombre","apellido_p","apellido_m","email","whatsapp","pais_destino","fecha_viaje","horario_cita","cliente")

    return Response({"estatus":"1","data":cita_nueva})



"""

    Regresa las citas de un cliente.
    Se valida a travez de whatsapp.
    Parametros:
        whatsapp:
"""
@api_view(['GET'])
def getCitas(request):
    email = request.GET.get("email")
    solo_activas = request.GET.get("solo_activas")
    page = request.GET.get("num_page")

    try:
        cliente = Cliente.objects.get(email = email)
    except: 
        return Response({"estatus":"0","msj":"El cliente ligado al correo electónico: " + email + ", no existe."})
    
    citas1 = Cita.objects.filter(cliente = cliente,estatus_cita = EstatusCita.objects.get(id=1))
    
    today = datetime.datetime.now().date()

    for c in citas1:
        if(c.horario_cita.fecha.fecha < today):
            c.estatus_cita = EstatusCita.objects.get(id = 2) # vencida
            c.save()

    print(solo_activas)
    if(solo_activas == "true"):
        estatus_activo = EstatusCita.objects.get(id = 1)
        citas = Cita.objects.filter(cliente = cliente,estatus_cita = estatus_activo).values("fecha_viaje","horario_cita__fecha__fecha","horario_cita__horario","pais_destino","estatus_cita__estatus","estatus_cita__id").order_by("-horario_cita__fecha__fecha","horario_cita__horario")
    else:
        citas = Cita.objects.filter(cliente = cliente).values("fecha_viaje","horario_cita__fecha__fecha","horario_cita__horario","pais_destino","estatus_cita__estatus","estatus_cita__id").order_by("-horario_cita__fecha__fecha","horario_cita__horario")
    
    p = Paginator(citas,5)

    print(p.get_page(page).previous_page_number)
    
    pagination = {
        "total_pages":p.num_pages
    }

    
    return Response({"estatus":"1","data":p.get_page(page).object_list,"pagination":pagination})

