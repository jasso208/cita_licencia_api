from django.db import models

class EstatusCita(models.Model):
    estatus = models.CharField(max_length = 20,null = False, blank = False)

    def __str__(self):
        return self.estatus