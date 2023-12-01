from django.db import models

class CatHorario(models.Model):
    consecutivo = models.CharField(max_length = 20)
    horario = models.CharField(max_length = 20)
    disponible = models.IntegerField()

    def __str__(self):
        return self.horario + " - " + str(self.disponible)