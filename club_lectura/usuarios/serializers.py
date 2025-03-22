from rest_framework import serializers
from django.contrib.auth.models import User
from libros.models import Genero, libro_grupo, libro_usuario
from .models import Detalle_usuario, Amistad, Notificaciones_amistad, Grupo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class LibroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = libro_usuario
        fields = '__all__'

class DetalleUsuarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    generos = GeneroSerializer(many=True)
    libros = LibroUsuarioSerializer()

    class Meta:
        model = Detalle_usuario
        fields = '__all__'

class AmistadSerializer(serializers.ModelSerializer):
    usuario_principal = UserSerializer()
    usuario_secundario = UserSerializer()

    class Meta:
        model = Amistad
        fields = '__all__'

class NotificacionesAmistadSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()
    usuario_solicitante = UserSerializer()

    class Meta:
        model = Notificaciones_amistad
        fields = '__all__'

class LibroGrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = libro_grupo
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    administrador = UserSerializer()
    miembros = UserSerializer(many=True)
    libro = LibroGrupoSerializer()

    class Meta:
        model = Grupo
        fields = '__all__'
