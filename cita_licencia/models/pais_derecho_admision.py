from django.db import models
from cita_licencia.models.pais import Pais

class PaisDerechoAdmision(models.Model):
    pais = models.OneToOneField(Pais,on_delete = models.PROTECT,null = False,blank = False)

    def __str__(self):
        return self.pais.descripcion
