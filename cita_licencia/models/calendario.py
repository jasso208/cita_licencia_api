from django.db import models

class Calendario(models.Model):
    fecha = models.DateField(unique = True)

    def __str__(self):
        return str(self.fecha)