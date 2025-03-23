from django.shortcuts import render
from usuarios.models import Detalle_usuario, Amistad, Notificaciones_amistad, Grupo
from .serializers import DetalleUsuarioSerializer, AmistadSerializer, NotificacionesAmistadSerializer, GrupoSerializer
from rest_framework import viewsets

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Detalle_usuario.objects.all()
    serializer_class = DetalleUsuarioSerializer

class DetalleUsuarioViewSet(viewsets.ModelViewSet):
    queryset = Detalle_usuario.objects.all()
    serializer_class = DetalleUsuarioSerializer

class AmistadViewSet(viewsets.ModelViewSet):
    queryset = Amistad.objects.all()
    serializer_class = AmistadSerializer

class NotificacionesAmistadViewSet(viewsets.ModelViewSet):
    queryset = Notificaciones_amistad.objects.all()
    serializer_class = NotificacionesAmistadSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer