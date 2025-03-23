from django.shortcuts import render
from rest_framework import viewsets
from .models import Resena, Autor, Genero, Saga, Libro, Estado_libro, libro_usuario, libro_grupo
from .serializer import ResenaSerializer, AutorSerializer, GeneroSerializer, SagaSerializer, LibroSerializer, EstadoLibroSerializer, UserSerializer, LibroUsuarioSerializer, LibroGrupoSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

class AurtorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class SagaViewSet(viewsets.ModelViewSet):
    queryset = Saga.objects.all()
    serializer_class = SagaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class EstadoLibroViewSet(viewsets.ModelViewSet):
    queryset = Estado_libro.objects.all()
    serializer_class = EstadoLibroSerializer

class LibroUsuarioViewSet(viewsets.ModelViewSet):
    queryset = libro_usuario.objects.all()
    serializer_class = LibroUsuarioSerializer

class LibroGrupoViewSet(viewsets.ModelViewSet):
    queryset = libro_grupo.objects.all()
    serializer_class = LibroGrupoSerializer