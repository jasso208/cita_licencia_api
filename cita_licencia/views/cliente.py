
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cita_licencia.models.cliente import Cliente

from cita_licencia.utils.token import Token
from cita_licencia.utils.email import Email


"""
    Genera token y lo envia por correo/whatsapp
"""
@api_view(['POST'])
def tokenCliente(request):
    whatsapp = "0"
    email = ""
    try:
        whatsapp = request.data["whatsapp"]    
    except:
        pass
    try:
        email = request.data["email"]
    except:
        pass
    
    if(whatsapp == ""):
        whatsapp = "0"
        
    if (email == "" and whatsapp == "0"):
        return Response({"estatus":0,"msj":"Debe indicar el Whatsapp o Email."})

    try:
        # Validamos la existencia del cliente por su whatsapp.
        if(whatsapp != "0"):
            cliente = Cliente.objects.get(whatsapp = int(whatsapp))    
            cliente.forma_autenticacion = 'W'    
    except:
        # Si el cliente no existe, lo creamos.
        cliente = Cliente()
        cliente.nombre_completo = ""
        cliente.email = email
        cliente.whatsapp = whatsapp
        cliente.forma_autenticacion = 'W'
        cliente.save()
        
    try:
        # Validamos la existencia del cliente por su email.
        if(email != ""):
            cliente = Cliente.objects.get(email = email)        
            cliente.forma_autenticacion = 'E'
    except:
        # Si el cliente no existe, lo creamos.
        cliente = Cliente()        
        cliente.nombre_completo = ""
        cliente.email = email
        cliente.whatsapp = whatsapp
        cliente.forma_autenticacion = 'E'
        cliente.save()

    """
        Almacena el token generado para autenticarse
    """
    t = Token()
    cliente.token = t.getToken()
    cliente.save()

    if(cliente.forma_autenticacion == 'E'):
        """
            Enviamos el email por correo
        """
        email = Email
        email.sendMail(cliente.token,cliente.email,"Citas ANA: Valida tu email")

    if(cliente.forma_autenticacion == 'W'):
        pass   

    return Response({"estatus":"1","id_cliente":cliente.id,"forma_autenticacion":cliente.forma_autenticacion})


"""
    Valida el token que se le envio al cliente por correo.
    Parametros: 
        token
        id_cliente
        forma_autenticacion: W:whatsapp; E:email
"""
@api_view(['GET'])
def validaTokenCliente(request):
    token = request.GET.get("token")
    id_cliente = request.GET.get("id_cliente")
    forma_autenticacion = request.GET.get("forma_autenticacion")
    try:
        cliente = Cliente.objects.get(id = id_cliente,token = token)
        if(forma_autenticacion == "E"):
            cliente.email_validado = 1
        
        if(forma_autenticacion == "W"):
            cliente.whatsapp_validado = 1
        
        #una vez validado el token, lo eliminamos para que no se vuelva a usar.
        cliente.token = ""
        
        cliente.save()

        data = {
            "id" : cliente.id,
            "nombre" : cliente.nombre,
            "apellido_p" : cliente.apellido_p,
            "apellido_m" : cliente.apellido_m,
            "whatsapp" : cliente.whatsapp,
            "email" : cliente.email,
            "pais_destino" : cliente.pais_destino,
            "fecha_viaje" : cliente.fecha_viaje,
            "whatsapp_validado":cliente.whatsapp_validado,
            "email_validado":cliente.email_validado
        }

        return Response({"estatus":"1","data":data})
    except:
        return Response({"estatus":"0","msj":"Token incorrecto"})
    
"""
    Actualiza la información del cliente.
"""
@api_view(['PUT'])
def actualizaCliente(request):
    try:
        id = request.data["id"]
        nombre = request.data["nombre"]
        apellido_p = request.data["apellido_p"]
        apellido_m = request.data["apellido_m"]
        whatsapp = request.data["whatsapp"]
        email = request.data["email"]
        pais_destino = request.data["pais_destino"]
        fecha_viaje = request.data["fecha_viaje"]
        
        try:
            cliente = Cliente.objects.get(id = id)
        except:
            return Response({"estatus":"0","msj":"El cliente no existe"})
        
        if(nombre != ""):
            cliente.nombre = nombre
        if(apellido_p != ""):
            cliente.apellido_p = apellido_p
        if(apellido_m != ""):
            cliente.apellido_m = apellido_m
        if(whatsapp != ""):
            cliente.email = email
        if(pais_destino != ""):
            cliente.pais_destino = pais_destino
        if(fecha_viaje != ""):
            cliente.fecha_viaje = fecha_viaje
        
        cliente.save()
        
        return Response({"estatus":"1","msj":"OK"})
    except:
        return Response({"estatus":"0","msj":"Error al actualizar el cliente."})

