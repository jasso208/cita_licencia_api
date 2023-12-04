from rest_framework.decorators import api_view
from rest_framework.response import Response
from cita_licencia.models.cliente import Cliente
from cita_licencia.models.horario_dia import HorarioDia
from cita_licencia.models.cita import Cita


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
    cita.save()

    hora_cita.cliente_reserva = cliente
    hora_cita.disponible = 0
    hora_cita.save()

    cita_nueva = Cita.objects.filter(id = cita.id).values("nombre","apellido_p","apellido_m","email","whatsapp","pais_destino","fecha_viaje","horario_cita","cliente")

    return Response({"estatus":"1","data":cita_nueva})

