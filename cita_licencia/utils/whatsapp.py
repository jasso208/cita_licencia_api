# -- coding: utf-8 --
import requests
from django.conf import settings

class Whatsapp():
    def sendWhatsapp(self,body,to):

        url = settings.URL
        token = settings.TOKEN
        payload = "token=" + token + "&to=" + str(to) + "&body=" + str(body)
        
        #payload = payload.encode('utf8').decode('iso-8859-1')        
        payload = payload.encode('utf8')
        
        headers = {'content-type': 'application/x-www-form-urlencoded'}


        response = requests.request("POST", url, data=payload, headers=headers)
        
        return response.json()["id"]

    def getClientId(self,idmsj):
        url = settings.URLMESSAGES
        token = settings.TOKEN

        querystring = {
            "token": token,
            "page": 1,
            "limit": 10,
            "status": "all",
            "sort": "desc",
            "id": idmsj,
            "referenceId": "",
            "from": "",
            "to": "",
            "ack": "",
            "msgId": "",
            "start_date": "",
            "end_date": ""
        }

        headers = {'content-type': 'application/x-www-form-urlencoded'}

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()["messages"][0]["to"]
        

    def msjConfirmacionCita(self,cita):
        body = ""
        body = body + "Buenos días, este es un recordatorio de: \n"
        body = body + "Su cita para el trámite del Permiso Internacional para Conducir. \n\n"

        body = body + "El día: "+ cita.horario_cita.fecha.fecha.strftime('%Y-%m-%d') +"\n"
        body = body + "A las: "+ cita.horario_cita.consecutivo +"\n"
        body = body + "En: Calle Durango 81, 4o Piso, Col. Roma Norte 06700 Ciudad de México CDMX, México. \n\n"

        body = body + "Para poder hacer el trámite necesita una copia de: \n"

        body = body + "Pasaporte vigente mínimo por un año \n"
        body = body + "Licencia mexicana vigente mínimo por un año (Licencia Física) \n"
        body = body + "IFE \n"
        body = body + "Comprobante de domicilio \n"
        body = body + "Una fotografía tamaño pasaporte a color \n"

        body = body + "El costo es de 1,300.00 y tiene de vigencia un año el pago es en efectivo a la entrega de su Documento \n"

        #body = body + "Le pedimos su apoyo para confirmar su asistencia \n"

        return body
