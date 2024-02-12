from django.db import models
from cita_licencia.models.pais import Pais

class PaisNoDestino(models.Model):
    pais = models.ForeignKey(Pais,on_delete=models.PROTECT,null=False,blank = False)