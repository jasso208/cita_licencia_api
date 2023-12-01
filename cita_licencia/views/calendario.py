from cita_licencia.models.calendario import Calendario
from cita_licencia.models.cat_horario import CatHorario
from cita_licencia.models.horario_dia import HorarioDia
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
            
    return Response({})
            