from django.db import models
from django.contrib.auth.models import User
from django.apps import apps
# Create your models here.

class Resena(models.Model):
    calificacion = models.IntegerField(default=1)

    def __str__(self):
        return f"Reseña {self.id} - {self.calificacion}/5"

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    biografia = models.TextField()
    fecha_nacimiento = models.DateField()
    imagen_autor = models.TextField(null=True, blank=True)
    resena = models.ForeignKey(Resena, on_delete=models.CASCADE, related_name='resena_autor')
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.nombre
    
class Genero(models.Model):
    nombre = models.CharField(max_length=50)
        
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        
        def __str__(self):
            return self.nombre
        
class Saga(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    numero_libros = models.IntegerField()
    imagen_saga = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Saga'
        verbose_name_plural = 'Sagas'

    def __str__(self):
        return self.nombre
    

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor,related_name='autor',on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero,related_name='genero',on_delete=models.CASCADE)
    sinopsis = models.TextField()
    portada = models.TextField(null=True, blank=True)
    fecha_publicacion = models.DateField()
    saga = models.ForeignKey(Saga,related_name='saga',on_delete=models.CASCADE)
    resena = models.ForeignKey(Resena, on_delete=models.CASCADE, related_name='resena_libro')
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
    
    def __str__(self):
        return self.titulo
    
class Estado_libro(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Estado de Libro'
        verbose_name_plural = 'Estados de Libros'

    def __str__(self):
        return f"{self.libro.titulo} - {self.usuario.username}"
    
class libro_usuario(models.Model):
    libro = models.ForeignKey(Libro,related_name='libro',on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,related_name='usuario',on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    comentario = models.TextField()
    estado = models.ForeignKey(Estado_libro,related_name='estado_usuario',on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Libro de Usuario'
        verbose_name_plural = 'Libros de Usuarios'
    
    def __str__(self):
        return f"{self.libro.titulo} - {self.usuario.username}"
    
class libro_grupo(models.Model):
    libro = models.ForeignKey(Libro,related_name='libro_grupo',on_delete=models.CASCADE)
    grupo = models.ForeignKey('usuarios.Grupo',related_name='grupo',on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    comentario = models.TextField()
    estado = models.ForeignKey(Estado_libro,related_name='estado_grupo',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Libro de Grupo'
        verbose_name_plural = 'Libros de Grupos'

    def __str__(self):
        return f"{self.libro.titulo} - {self.grupo.nombre}"
