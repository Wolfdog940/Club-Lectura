from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plantilla(models.Model):
    nombre = models.CharField(max_length=100)
    mensaje = models.TextField()
    
    class Meta:
        verbose_name = 'Plantilla'
        verbose_name_plural = 'Plantillas'
    
    def __str__(self):
        return self.nombre


class Correo(models.Model):
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    destinatario = models.ForeignKey(User,max_length=100, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Correo'
        verbose_name_plural = 'Correos'
    
    def __str__(self):
        return self.asunto
    

