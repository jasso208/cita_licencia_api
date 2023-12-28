

from rest_framework.decorators import api_view
from rest_framework.response import Response

from cita_licencia.models.pais import Pais

@api_view(["GET"])
def getAllPais(request):
    catP = Pais.objects.all().values("id","cve_pais","descripcion")

    return Response ({"estatus":"1","data":catP})
