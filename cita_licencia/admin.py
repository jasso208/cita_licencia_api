from django.contrib import admin
from .models.cliente import Cliente
from .models.calendario import Calendario
from .models.cat_horario import CatHorario
from .models.horario_dia import HorarioDia
from .models.cita import Cita

admin.site.register(Cliente)
admin.site.register(Calendario)
admin.site.register(CatHorario)
admin.site.register(HorarioDia)
admin.site.register(Cita)