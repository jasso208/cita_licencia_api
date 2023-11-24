from django.http import JsonResponse
from .models.cliente import Cliente

def getClientes(request):
    cliente = Cliente.objects.all()
    data = list(cliente.values("id","email","whatsapp"))
    return JsonResponse(data,safe = False)
