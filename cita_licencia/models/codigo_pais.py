from django.db import models

class CodigoPais(models.Model):
    nombre = models.CharField(max_length=30,null=False,blank=False)
    nombre_corto = models.CharField(max_length=5,null=False,blank=False)
    codigo = models.CharField(max_length=5,null=False,blank = True)

    