from django.db import models

class Participante(models.Model):
    dni = models.IntegerField()
    mail = models.EmailField()
    def __str__(self):
        return str(self.dni)


class Grupo(models.Model):
    part = models.ForeignKey(Participante,on_delete=models.SET_NULL,null = True)
    tamaño = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)

class Expediente(models.Model):
    mediador1 = models.ForeignKey('auth.User',on_delete=models.SET_NULL,null=True)
    # mediador2 = models.ForeignKey('auth.User',on_delete=models.SET_NULL,null=True)
    numero = models.IntegerField(db_index=True)
    nombre = models.CharField(max_length=100)
    grup = models.ForeignKey(Grupo,on_delete=models.SET_NULL,null = True)
    
    def __str__(self):
        return 'N° {}. {}'.format(self.numero, self.nombre)

class Audiencia(models.Model):
    fecha = models.DateTimeField(db_index = True, blank=True ,null=True)
    exp = models.ForeignKey('Expediente',on_delete=models.SET_NULL,null=True)
    grup = models.ForeignKey(Grupo,on_delete=models.CASCADE,default = exp)
    def __str__(self):
        return str(self.fecha)
        
