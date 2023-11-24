from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_completo = models.CharField(max_length = 100,null  = True,blank = True)
    whatsapp = models.IntegerField(max_length = 10,null  = False,blank = False)
    email = models.EmailField(max_length = 200,null  = False,blank = False)
    pais_destino = models.CharField(max_length = 50,null  = True,blank = True)
    fecha_viaje = models.DateField(null  = True,blank = True)

    def __str__(self):
        return self.email
