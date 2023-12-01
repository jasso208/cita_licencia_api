
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cita_licencia.models.cliente import Cliente


'''
    Almacena cliente:
        llave: 
            whatsapp, email
        * Al identificarse, el cliente debe ingresar al menos whatsapp e el email.
        * Mientras un email o whatsapp no este confirmado puede ser usado por otro cliente. 
        * Una vez que el cliente haya generado una cita contara como confirmado, y su correo y whatsapp no podran ser usado por otro cliente.
        * 
'''
@api_view(['POST'])
def validaCliente(request):
    whatsapp = ""
    email = ""
    try:
        whatsapp = request.data["whatsapp"]    
    except:
        pass
    try:
        email = request.data["email"]
    except:
        pass

    if (email == "" and whatsapp == ""):
        return Response({"estatus":0,"msj":"Debe indicar el Whatsapp o Email."})

    try:
        # Validamos la existencia del cliente por su whatsapp.
        if(whatsapp != ""):
            cliente = Cliente.objects.get(whatsapp = whatsapp)        
    except:
        # Si el cliente no existe, lo creamos.
        cliente = Cliente()
        cliente.nombre_completo = ""
        cliente.email = email
        cliente.whatsapp = whatsapp
        cliente.save()
        
    try:
        # Validamos la existencia del cliente por su email.
        if(email != ""):
            cliente = Cliente.objects.get(email = email)        
    except:
        # Si el cliente no existe, lo creamos.
        cliente = Cliente()        
        cliente.nombre_completo = ""
        cliente.email = email
        cliente.whatsapp = whatsapp
        cliente.save()

    return Response({"estatus":"1","id_cliente":cliente.id})


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

