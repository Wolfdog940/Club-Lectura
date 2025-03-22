from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Resena, Autor, Genero, Saga, Libro, Estado_libro, 
    libro_usuario, libro_grupo
)
from usuarios.models import Grupo  # Importa el modelo de Grupo

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    resena = ResenaSerializer()

    class Meta:
        model = Autor
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class SagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saga
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    genero = GeneroSerializer()
    saga = SagaSerializer()
    resena = ResenaSerializer()

    class Meta:
        model = Libro
        fields = '__all__'

class EstadoLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_libro
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class LibroUsuarioSerializer(serializers.ModelSerializer):
    libro = LibroSerializer()
    usuario = UserSerializer()
