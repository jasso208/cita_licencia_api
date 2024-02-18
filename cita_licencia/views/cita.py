from rest_framework.decorators import api_view
from rest_framework.response import Response
from cita_licencia.models.cliente import Cliente
from cita_licencia.models.horario_dia import HorarioDia
from cita_licencia.models.cita import Cita
from cita_licencia.models.estatus_cita import EstatusCita
from django.core.paginator import Paginator
from cita_licencia.models.pais import Pais
from cita_licencia.models.codigo_pais import CodigoPais

from cita_licencia.utils.email import Email

from cita_licencia.utils.whatsapp import Whatsapp
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
    codigo_pais = request.data["codigo_pais"]
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
    

    wcoi = cliente.codigo_pais.codigo + cliente.whatsapp

    cp = CodigoPais
    try:
        cp = CodigoPais.objects.get(id = codigo_pais)
    except:
        pass
    
    wcoip = cp.codigo + whatsapp

    if(cliente.whatsapp != None and cliente.whatsapp != 0):
        #if(str(cliente.whatsapp).strip() != whatsapp.strip() or cliente.email.strip() != email.strip()):
        if(wcoip.strip() != wcoi.strip() or cliente.email.strip() != email.strip()):
            return Response({"estatus":"0","msj":"El email y/o whatsapp no corresponden con el cliente indicado."})
    else:
        if(cliente.email.strip() != email.strip()):
            return Response({"estatus":"0","msj":"El email no corresponden con el cliente indicado."})
    
    try:
        print(pais_destino)
        pais = Pais.objects.get(id = pais_destino)
    except:
        return Response({"estatus":"0","msj":"País no valido."})

    cita = Cita()
    cita.nombre = nombre
    cita.apellido_p = apellido_p
    cita.apellido_m = apellido_m
    cita.codigo_pais = cp
    cita.whatsapp = whatsapp
    cita.email = email
    cita.pais_destino = pais
    cita.fecha_viaje = fecha_viaje
    cita.cliente = cliente
    cita.horario_cita = hora_cita
    cita.estatus_cita = EstatusCita.objects.get(id=1)
    cita.save()

    hora_cita.cliente_reserva = cliente
    hora_cita.disponible = 0
    hora_cita.save()

    cita_nueva = Cita.objects.filter(id = cita.id).values("id","nombre","apellido_p","apellido_m","email","whatsapp","codigo_pais__id","pais_destino","fecha_viaje","horario_cita","cliente")


    #Envia confirmación de cita
    email = Email()
    body = email.plantillaConfirmacionCita(cita);
    err = email.sendMail(body,cliente.email,"Confirmación de cita")
        
    whatsapp = Whatsapp()
    wapp = cliente.codigo_pais.codigo + cliente.whatsapp
    #body = "Se agendo su cita para el dia  " + cita.horario_cita.fecha.fecha.strftime('%Y-%m-%d') + " de " +cita.horario_cita.horario
    
    body = whatsapp.msjConfirmacionCita(cita)
    
    idmsj = whatsapp.sendWhatsapp(body,wapp)

    return Response({"estatus":"1","data":cita_nueva})




"""
    Genera nueva cita.
        Parametros            
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
def generaCitaAdministrador(request):
    #id_cliente = request.data["id_cliente"]
    id_horario_cita = request.data["id_horario_cita"]
    nombre = request.data["nombre"]
    apellido_p = request.data["apellido_p"]
    apellido_m = request.data["apellido_m"]
    codigo_pais = request.data["codigo_pais"]
    whatsapp = request.data["whatsapp"]
    email = request.data["email"]
    pais_destino = request.data["pais_destino"]
    fecha_viaje = request.data["fecha_viaje"]

    """
    try:
        cliente = Cliente.objects.get(id = id_cliente)
    except:
        return Response({"estatus":"0","msj":"Error al generar la cita. Cliente no existe."})
    """

    try:
        hora_cita = HorarioDia.objects.get(id = id_horario_cita,cliente_reserva = None)
    except:
        return Response({"estatus":"0","msj":"Error al generar la cita. Horario no disponible."})
    
    
    try:
        cp = CodigoPais.objects.get(id = codigo_pais)
    except:
        return Response({"estatus":"0","msj":"Error al generar la cita. El código internacional del whatsapp no es valido."})

    #1: Validamos si existe un cliente con el whatsapp y correo y ambos verificados.
    try:
        #Si encontramos el cliente con el whatsapp y email valiado, sera al que se le generara la cita.
        cliente = Cliente.objects.get(email = email.strip(), codigo_pais = cp, whatsapp = whatsapp.strip(),whatsapp_validado=1 , email_validado=1)
    except:
        #Validamos si el whatsapp y el email se validaron en cuantas diferentes.
        try:
            #si no encuentra el cliente con el email validado, continuamos normalmente
            cliente_email = Cliente.objects.get(email = email.strip(),email_validado = 1)   

            #Si el cliente ya ha validado el email
            #validamos que si ya no haya confirmado el whatsapp
            #si tiene whatsapp validado, esto seria incorrecto ya que anteriormente se valido que el whatsapp del parametro y el email correspondan al mismo
            if cliente_email.whatsapp_validado == 1:
                return Response({"estatus":"0","msj":"Error al generar la cita. El cliente ya ha verificado el número de whatsapp " + cliente_email.codigo_pais.codigo + cliente_email.whatsapp + "."})                    
        except:
            cliente_email = None
            
        try:
            #si no encuentra el cliente con el whatsapp validado, continuamos normalmente
            cliente_whatsapp = Cliente.objects.get(whatsapp = whatsapp.strip(),email_validado = 1)            
        except:
            cliente_whatsapp = None
        
        if cliente_whatsapp != None and cliente_email!= None:
            # si el cliente que valido el email es diferente al cliente que valido el whatsapp, son diferentes, no permite generar la cita.
            if cliente_whatsapp != cliente_email:
                cl_w = cliente_whatsapp.nombre + ' ' + cliente_whatsapp.apellido_p + ' ' + cliente_whatsapp.apellido_m
                cl_e = cliente_email.nombre + ' ' + cliente_email.apellido_p + ' ' + cliente_email.apellido_m
                
                msj = "Error al generar la cita. El número de whatsapp indicado ha sido registrado por el cliente " + cl_w + " y "
                msj = msj + " el email ha sido registrado por el cliente " + cl_e + "."
                return Response({"estatus":"0","msj":msj})
        
        if cliente_email != None and cliente_whatsapp == None:
            #Si el email ha sido validado por un cliente, y el whatsapp no ha sido validado, usamos el cliente que valido el email
            # y le asignamos el whatsapp que recibimos como parametro, lo marcamos como asignado.
            cliente = cliente_email
            cliente.whatsapp = whatsapp.strip()
            cliente.codigo_pais = cp
            cliente.whatsapp_validado = 1
            cliente.save()

        #Este escenario no deberia pasar, pero igual lo contemplamos.
        if cliente_email == None and cliente_whatsapp != None:
            #Si el whatsapp ha sido validado por un cliente, y el email no ha sido validado, usamos el cliente que valido el whatsapp
            # y le asignamos el email que recibimos como parametro, lo marcamos como asignado.
            cliente = cliente_whatsapp
            cliente.email = email.strip()            
            cliente.email_validado = 1
            cliente.save()
    
    try:
        cita_activa = EstatusCita.objects.get(id = 1)
        Cita.objects.get(cliente = cliente,estatus_cita = cita_activa)
        cl_nom = cliente.nombre + ' ' + cliente.apellido_p + ' ' + cliente.apellido_m
        return Response({"estatus":"0","msj":"El cliente identificado con el whatsapp " + cp.codigo + whatsapp + " y email "+ email + " (" + cl_nom + ") ya cuenta con una cita activa."})
    except:
        pass 
    
    wcoip = cp.codigo + whatsapp
    
    try:        
        pais = Pais.objects.get(id = pais_destino)
    except:
        return Response({"estatus":"0","msj":"País destino no valido."})

    cita = Cita()
    cita.nombre = nombre
    cita.apellido_p = apellido_p
    cita.apellido_m = apellido_m
    cita.codigo_pais = cp
    cita.whatsapp = whatsapp
    cita.email = email
    cita.pais_destino = pais
    cita.fecha_viaje = fecha_viaje
    cita.cliente = cliente
    cita.horario_cita = hora_cita
    cita.estatus_cita = EstatusCita.objects.get(id=1)
    cita.save()

    hora_cita.cliente_reserva = cliente
    hora_cita.disponible = 0
    hora_cita.save()

    cita_nueva = Cita.objects.filter(id = cita.id).values("id","nombre","apellido_p","apellido_m","email","whatsapp","codigo_pais__id","pais_destino","fecha_viaje","horario_cita","cliente")


    #Envia confirmación de cita
    email = Email()
    body = email.plantillaConfirmacionCita(cita);
    err = email.sendMail(body,cliente.email,"Confirmación de cita")
        
    whatsapp = Whatsapp()
    wapp = cliente.codigo_pais.codigo + cliente.whatsapp
    #body = "Se agendo su cita para el dia  " + cita.horario_cita.fecha.fecha.strftime('%Y-%m-%d') + " de " +cita.horario_cita.horario
    body = whatsapp.msjConfirmacionCita(cita)
    idmsg= whatsapp.sendWhatsapp(body,wapp)

    return Response({"estatus":"1","data":cita_nueva})



"""
    Consulta cita
"""
@api_view(["GET"])
def consultaCita(request):
    id_cita = request.GET.get("id_cita")
    
    cita = Cita.objects.filter(id = id_cita).values("nombre","apellido_p","apellido_m","email","whatsapp","codigo_pais__id","pais_destino__id","fecha_viaje","horario_cita__id","horario_cita__horario","horario_cita__consecutivo","horario_cita__fecha__fecha","cliente")
    
    return Response({"estatus":"1","data":cita})


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
    
    print(cliente.id)
    citas1 = Cita.objects.filter(cliente = cliente,estatus_cita = EstatusCita.objects.get(id=1))
    
    print(citas1)
    today = datetime.datetime.now().date()

    for c in citas1:
        if(c.horario_cita.fecha.fecha < today):
            c.estatus_cita = EstatusCita.objects.get(id = 2) # vencida
            c.save()

    if(solo_activas == "true"):
        estatus_activo = EstatusCita.objects.get(id = 1)
        citas = Cita.objects.filter(cliente = cliente,estatus_cita = estatus_activo).values("id","fecha_viaje","horario_cita__fecha__fecha","horario_cita__horario","pais_destino__descripcion","estatus_cita__estatus","estatus_cita__id").order_by("estatus_cita__id","-horario_cita__fecha__fecha","horario_cita__horario","-id")
    else:
        citas = Cita.objects.filter(cliente = cliente).values("id","fecha_viaje","horario_cita__fecha__fecha","horario_cita__horario","pais_destino__descripcion","estatus_cita__estatus","estatus_cita__id").order_by("estatus_cita__id","-horario_cita__fecha__fecha","horario_cita__horario","-id")
    
    print(citas)
    p = Paginator(citas,5)

    print(p.get_page(page).previous_page_number)
    
    pagination = {
        "total_pages":p.num_pages
    }

    
    return Response({"estatus":"1","data":p.get_page(page).object_list,"pagination":pagination})


"""

    Regresa todas las citas
    es consumido desde el perfil de administrador.
    parametros:
        fecha
        whatsapp/email
        solo_activas
"""
@api_view(['GET'])
def getAllCitas(request):
    fecha = request.GET.get("fecha")
    solo_activas = request.GET.get("solo_activas")
    page = request.GET.get("num_page")
   
    print(fecha)
    citas1 = Cita.objects.filter(horario_cita__fecha__fecha = fecha)
    
    today = datetime.datetime.now().date()

    for c in citas1:
        if(c.horario_cita.fecha.fecha < today):
            c.estatus_cita = EstatusCita.objects.get(id = 2) # vencida
            c.save()

    if(solo_activas == "true"):
        estatus_activo = EstatusCita.objects.get(id = 1)
        citas = Cita.objects.filter(horario_cita__fecha__fecha = fecha,estatus_cita = estatus_activo).values("id","fecha_viaje","horario_cita__fecha__fecha","horario_cita__horario","pais_destino__descripcion","estatus_cita__estatus","estatus_cita__id").order_by("estatus_cita__id","-horario_cita__fecha__fecha","horario_cita__horario","-id")
    else:
        citas = Cita.objects.filter(horario_cita__fecha__fecha = fecha).values("id","fecha_viaje","horario_cita__fecha__fecha","horario_cita__horario","pais_destino__descripcion","estatus_cita__estatus","estatus_cita__id").order_by("estatus_cita__id","-horario_cita__fecha__fecha","horario_cita__horario","-id")
    
    p = Paginator(citas,5)

    print(p.get_page(page).previous_page_number)
    
    pagination = {
        "total_pages":p.num_pages
    }

    
    return Response({"estatus":"1","data":p.get_page(page).object_list,"pagination":pagination})






"""
Actualiza cita
"""
@api_view(["PUT"])
def actualizaCita(request):
    id_cita = request.data["id_cita"]
    id_horario_cita = request.data["id_horario_cita"]
    nombre = request.data["nombre"]
    apellido_p = request.data["apellido_p"]
    apellido_m = request.data["apellido_m"]
    whatsapp = request.data["whatsapp"]
    email = request.data["email"]
    pais_destino = request.data["pais_destino"]
    fecha_viaje = request.data["fecha_viaje"]
    cancelar_cita = request.data["cancelar_cita"]
    
    try:
        cita = Cita.objects.get(id = id_cita)
    except:
        return Response({"estatus":"0","msj":"Error al actualizar la cita. Cita no encontrada."})

    if(cita.horario_cita.id != id_horario_cita):
        try:
            hora_cita = HorarioDia.objects.get(id = id_horario_cita,disponible = 1)
        except:
            return Response({"estatus":"0","msj":"Error al actualizar la cita. Horario no disponible."})
    else:
        hora_cita = cita.horario_cita


    try:
        pais = Pais.objects.get(id = pais_destino)
    except:
        return Response({"estatus":"0","msj":"País destino no valido."})

    #Volvemos a poner disponible la el horario que tenia la cita
    cita.horario_cita.disponible = 1
    cita.horario_cita.cliente_reserva = None
    cita.horario_cita.save()


    if(cancelar_cita == 1):
        cita.estatus_cita = EstatusCita.objects.get(id=3)  #cancelada
        cita.save()
        return Response({"estatus":"1","msj":"Cita cancelada correctamente."})
    
    cita.nombre = nombre
    cita.apellido_p = apellido_p
    cita.apellido_m = apellido_m
    #cita.whatsapp = whatsapp
    #cita.email = email
    cita.pais_destino = pais
    cita.fecha_viaje = fecha_viaje
    cita.horario_cita = hora_cita
    cita.estatus_cita = EstatusCita.objects.get(id=1) #activa
    cita.save()

    hora_cita.cliente_reserva = cita.cliente
    hora_cita.disponible = 0
    hora_cita.save()

    cita_nueva = Cita.objects.filter(id = cita.id).values("nombre","apellido_p","apellido_m","email","whatsapp","codigo_pais__id","pais_destino__id","fecha_viaje","horario_cita","cliente")

    return Response({"estatus":"1","data":cita_nueva})


@api_view(["GET"])
def validaClienteConCita(request):
    id_cliente = request.GET.get("id_cliente")

    cliente = Cliente.objects.get(id=id_cliente)

    activa = EstatusCita.objects.get(id=1)

    
    cita = Cita.objects.filter(cliente = cliente,estatus_cita = activa)
    

    if cita.count() >= 1:
        return Response({"estatus":"0","msj":"Ya cuenta con una cita activa."})
    else:
        return Response({"estatus":"1"})
    

