
from django.db import models

class Pais(models.Model):
    cve_pais = models.CharField(max_length = 10,null = False,blank = False)
    descripcion = models.CharField(max_length=50,null=False,blank = False)

    def __str__(self):
        return self.descripcion