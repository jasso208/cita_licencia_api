from cita_licencia.models.calendario import Calendario
from cita_licencia.models.cat_horario import CatHorario
from cita_licencia.models.horario_dia import HorarioDia
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
import datetime

@api_view(["POST"])
def cargaDiasMes(request):
    month = request.data["month"]
    year = request.data["year"]
    
    for day in range(32):
        try:
            fecha = datetime.date(year,month,day)
            calendario = Calendario()
            calendario.fecha = fecha
            calendario.save()

            cath = CatHorario.objects.all()
            print(cath)
            for c in cath:
                hd = HorarioDia()
                hd.consecutivo = c.consecutivo
                hd.disponible = c.disponible
                hd.horario = c.horario
                hd.fecha = calendario
                hd.save()
        except Exception as e:
            print(e)

        calendario = HorarioDia.objects.filter(fecha__fecha__year = year,fecha__fecha__month = month,disponible = 1,cliente_reserva = None).values("fecha__fecha").annotate(horarios_disponibles = Count("fecha")).order_by("fecha")

    return Response({"estatus":"1","data":calendario})


"""
    Regresa los horarios disponibles para cita de una fecha determinada
    parametros:
        fecha
"""
@api_view(["GET"])
def getHorariosLibres(request):
    fecha = request.GET.get("fecha")
    fechac = Calendario.objects.get(fecha = fecha)
    hr = HorarioDia.objects.filter(fecha = fechac,disponible = 1,cliente_reserva = None).values("id","horario")
    return Response({"estatus":"1","data":hr})


            