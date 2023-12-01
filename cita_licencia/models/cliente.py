from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100,null  = True,blank = True,default = "")
    apellido_p = models.CharField(max_length = 100, null = True,blank = True,default  = "")
    apellido_m = models.CharField(max_length = 100,null = True,blank = True,default = "")
    whatsapp = models.IntegerField(max_length = 10,null  = True,blank = True)
    email = models.EmailField(max_length = 200,null  = True,blank = True)
    pais_destino = models.CharField(max_length = 50,null  = True,blank = True)
    fecha_viaje = models.DateField(null  = True,blank = True)
    token = models.CharField(max_length = 14,null = True,blank = True)


    def __str__(self):
        if(self.nombre == ""):
            return "No name"
        return self.nombre + " " + self.apellido_p + " " + self.apellido_m

    def save(self, *args, **kwargs):        
        return super(Cliente,self).save()
