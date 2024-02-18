from rest_framework.decorators import api_view
from rest_framework.response import Response
from cita_licencia.models.cliente import Cliente
from cita_licencia.models.cita import Cita
from cita_licencia.models.estatus_cita import EstatusCita
from cita_licencia.utils.whatsapp import Whatsapp

@api_view(["POST"])
def wh_confirmacita(request):
    print("jasso")
    clientew = request.data["data"]["from"]
    print(clientew)
    body = request.data["data"]["body"]
    try:
        cliente = Cliente.objects.get(cliente_w = clientew)
    except Exception as e:
        print(str(e))
        print("no cliente")
        return Response({"NO CLIENTE"})
    
    estatusa = EstatusCita.objects.get(id = 1)
    try:
        cita = Cita.objects.get(cliente = cliente,estatus_cita = estatusa)
    except:
        print("No cita")
        return Response({"NO CITA"})


    if cita.espera_confirmacion == 0:
        print("No espera confirmación")
        return Response({"NO ESPERA CONFIRMACIÓN"})
    
    wh = Whatsapp()
    whn = cliente.codigo_pais.codigo + cliente.whatsapp
    if body.upper() != 'SI' and body.upper() != 'NO':
        print("Respuesta no valida, ¿Confirma la asistencia a su cita? (SI/NO).")
        msg = "Respuesta no valida, ¿Confirma la asistencia a su cita? (SI/NO)."        
        wh.sendWhatsapp(msg,whn)
        return Response({"RESPUESA INCORRECTA"})

    try:
        if body.upper() == 'SI':
            #solo debe tener una cita activa
            cita = Cita.objects.get(cliente = cliente,estatus_cita = estatusa)
            cita.cita_confirmada = 1
            cita.save()

            print("Cita confirmada.")
            msg = "Cita confirmada."        
            wh.sendWhatsapp(msg,whn)
            
            print("CITA CONFIRMADA")
            return Response({"CITA CONFIRMADA"})
        else:
            
            print("Su cita fue cancelada.")
            msg = "Su cita fue cancelada."        
            wh.sendWhatsapp(msg,whn)
            return Response({"CITA CANCELADA"})

    except:
        print("Error al confirmar si cita.")
        msg = "Error al confirmar si cita."        
        wh.sendWhatsapp(msg,whn)
        return Response({"ERROR CONFIRMACIÓN"})

    return Response({""})