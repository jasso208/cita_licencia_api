import requests
from django.conf import settings

class Whatsapp():
    def sendWhatsapp(self,body,to):
        
        url = settings.URL
        token = settings.TOKEN
        payload = "token=" + token + "&to=" + str(to) + "&body=" + str(body)
        payload = payload.encode('utf8').decode('iso-8859-1')
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)