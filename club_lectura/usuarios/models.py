
from django.db import models
from django.contrib.auth.models import User
from libros.models import Genero, libro_grupo, libro_usuario

class Detalle_usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='detalle_usuario')
    imagen_perfil = models.TextField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    generos = models.ManyToManyField(Genero, related_name='generos_usuario')
    libros = models.ForeignKey(libro_usuario, related_name='libros_usuario', on_delete=models.CASCADE, null=True, blank=True)
    accepta_notificaciones = models.BooleanField(default=True)

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


class Notificaciones_amistad(models.Model):
    usuario = models.ForeignKey(User, related_name='notificaciones_amistad', on_delete=models.CASCADE)
    usuario_solicitante = models.ForeignKey(User, related_name='notificaciones_amistad_solicitante', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aceptada = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notificación de amistad'
        verbose_name_plural = 'Notificaciones de amistad'

    def __str__(self):
        return f"{self.usuario.username} ha recibido una solicitud de amistad de {self.usuario_solicitante.username}"
    
class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    imagen_grupo = models.TextField(null=True, blank=True)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    administrador = models.ForeignKey(User, related_name='grupo_administrador', on_delete=models.CASCADE)
    miembros = models.ManyToManyField(User, related_name='grupo_miembros')
    libro = models.ForeignKey(libro_grupo, related_name='grupo_libros', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
    
    def __str__(self):
        return self.nombre