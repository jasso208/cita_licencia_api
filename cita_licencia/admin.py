from django.contrib import admin
from .models.cliente import Cliente
from .models.calendario import Calendario
from .models.cat_horario import CatHorario
from .models.horario_dia import HorarioDia
from .models.cita import Cita
from .models.estatus_cita import EstatusCita
from .models.pais import Pais
from .models.pais_derecho_admision import PaisDerechoAdmision
from .models.codigo_pais import CodigoPais
from .models.pais_no_destino import PaisNoDestino

admin.site.register(Cliente)
admin.site.register(Calendario)
admin.site.register(CatHorario)
admin.site.register(HorarioDia)
admin.site.register(Cita)
admin.site.register(EstatusCita)
admin.site.register(Pais)
admin.site.register(PaisDerechoAdmision)
admin.site.register(PaisNoDestino)
admin.site.register(CodigoPais)