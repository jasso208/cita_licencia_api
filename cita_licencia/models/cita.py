from django.db import models
from cita_licencia.models.cliente import Cliente
from cita_licencia.models.horario_dia import HorarioDia
from cita_licencia.models.estatus_cita import EstatusCita
from cita_licencia.models.pais import Pais
from cita_licencia.models.codigo_pais import CodigoPais
class Cita(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete = models.PROTECT,null = False,blank = False)
    horario_cita = models.ForeignKey(HorarioDia,on_delete = models.PROTECT,null = False,blank = False)
    nombre = models.CharField(max_length = 100,null  = True,blank = True,default = "")
    apellido_p = models.CharField(max_length = 100, null = True,blank = True,default  = "")
    apellido_m = models.CharField(max_length = 100,null = True,blank = True,default = "")
    codigo_pais = models.ForeignKey(CodigoPais,null=True,blank = True,on_delete = models.PROTECT)
    whatsapp = models.CharField(max_length = 15,null  = True,blank = True)
    email = models.EmailField(max_length = 200,null  = True,blank = True)
    #pais_destino = models.CharField(max_length = 50,null  = True,blank = True)
    pais_destino =models.ForeignKey(Pais,null = True,blank = True,on_delete = models.PROTECT)
    fecha_viaje = models.DateField(null  = True,blank = True)
    estatus_cita = models.ForeignKey(EstatusCita,null = True, blank = True,on_delete = models.PROTECT)
    espera_confirmacion = models.IntegerField(default = 0)
    cita_confirmada = models.IntegerField(default = 0)

  

