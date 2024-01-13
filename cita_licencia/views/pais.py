

from rest_framework.decorators import api_view
from rest_framework.response import Response
from cita_licencia.models.pais_derecho_admision import PaisDerechoAdmision
from cita_licencia.models.pais import Pais
from cita_licencia.models.codigo_pais import CodigoPais
@api_view(["GET"])
def getAllPais(request):
    catP = Pais.objects.all().values("id","cve_pais","descripcion")

    return Response ({"estatus":"1","data":catP})


"""
    Recibe un idpais y valida si este pais se reserva el derecho de admisión.
    paramemtros:
        id_pais
"""
@api_view(["GET"])
def validaPaisDerechoAdmision(request):
    id_pais = request.GET.get("id_pais")

    try:
        pais = Pais.objects.get(id = id_pais)
    except:
        return Response({"estatus":"0","msj":"Pais no valido."})
    
    try:
        PaisDerechoAdmision.objects.get(pais = pais)
        return Response({"estatus":"1","pais_derecho_admision":"1"})
    except:    
        return Response({"estatus":"1","pais_derecho_admision":"0"})

@api_view(["GET"])
def getAllCodigoTelPais(request):
    codigos = CodigoPais.objects.all().values("id","nombre_corto","codigo")
    return Response({"estatus":"1","data":codigos})



