from django.shortcuts import render
from rest_framework import viewsets
from .models import Resena, Autor, Genero, Saga, Libro, Estado_libro, libro_usuario, libro_grupo
from .serializer import ResenaSerializer, AutorSerializer, GeneroSerializer, SagaSerializer, LibroSerializer, EstadoLibroSerializer, LibroUsuarioSerializer, LibroGrupoSerializer
from rest_framework.permissions import IsAuthenticated

class ResenaViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

class AurtorViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class SagaViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Saga.objects.all()
    serializer_class = SagaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class EstadoLibroViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Estado_libro.objects.all()
    serializer_class = EstadoLibroSerializer

class LibroUsuarioViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = libro_usuario.objects.all()
    serializer_class = LibroUsuarioSerializer

class LibroGrupoViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = libro_grupo.objects.all()
    serializer_class = LibroGrupoSerializer