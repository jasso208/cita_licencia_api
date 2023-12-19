from django.db import models
from .calendario import Calendario
from .cliente import Cliente

class HorarioDia(models.Model):
    fecha = models.ForeignKey(Calendario,on_delete = models.CASCADE)
    consecutivo = models.CharField(max_length = 20)
    horario = models.CharField(max_length = 20)
    disponible = models.IntegerField()
    cliente_reserva = models.ForeignKey(Cliente,on_delete = models.PROTECT,null = True,blank = True)


    def __str__(self):
        return str(self.fecha.fecha) + "  " + str(self.consecutivo) + "  " + str(self.horario) + "  " + str(self.disponible)