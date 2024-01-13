from django.db import models

class CodigoPais(models.Model):
    nombre_corto = models.CharField(max_length=5,null=False,blank=False)
    codigo = models.CharField(max_length=5,null=False,blank = True)

    def __str__(self):
        return self.codigo

