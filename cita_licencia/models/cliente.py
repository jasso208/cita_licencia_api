from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100,null  = True,blank = True,default = "")
    apellido_p = models.CharField(max_length = 100, null = True,blank = True,default  = "")
    apellido_m = models.CharField(max_length = 100,null = True,blank = True,default = "")
    whatsapp = models.CharField(max_length = 15,null  = True,blank = True)
    whatsapp_validado = models.IntegerField(default = 0)#1 para indicar que ya se valido el whatsapp
    email = models.EmailField(max_length = 200,null  = True,blank = True)
    email_validado = models.IntegerField(default = 0) #1 para indicar que ya se valido  el email
    pais_destino = models.CharField(max_length = 50,default = "")
    fecha_viaje = models.DateField(null  = True,blank = True)
    token = models.CharField(max_length = 14,null = True,blank = True)
    forma_autenticacion = models.CharField(max_length = 1,null = True, blank = True)
    administrador = models.CharField(max_length = 1,default = 0)
    
    class Meta:
        unique_together = ('whatsapp','email')
        
    def __str__(self):
        if(self.nombre == ""):
            return "No name"
        return self.nombre + " " + self.apellido_p + " " + self.apellido_m

    def save(self, *args, **kwargs):        
        return super(Cliente,self).save()
