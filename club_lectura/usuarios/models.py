
from django.db import models
from django.contrib.auth.models import User

class DetalleUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='detalle_usuario')
    imagen_perfil_base64 = models.TextField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Detalle de Usuario'
        verbose_name_plural = 'Detalles de Usuarios'
    
    def __str__(self):
        return self.user.username


class Amistad(models.Model):
    usuario_principal = models.ForeignKey(User, related_name='amistades_principales', on_delete=models.CASCADE)
    usuario_secundario = models.ForeignKey(User, related_name='amistades_secundarias', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario_principal', 'usuario_secundario')

    def __str__(self):
        return f"{self.usuario_principal.username} es amigo de {self.usuario_secundario.username}"

