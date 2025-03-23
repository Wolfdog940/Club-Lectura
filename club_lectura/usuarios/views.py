from django.shortcuts import render
from usuarios.models import Detalle_usuario, Amistad, Notificaciones_amistad, Grupo
from .serializers import DetalleUsuarioSerializer, AmistadSerializer, NotificacionesAmistadSerializer, GrupoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Detalle_usuario.objects.all()
    serializer_class = DetalleUsuarioSerializer

class DetalleUsuarioViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Detalle_usuario.objects.all()
    serializer_class = DetalleUsuarioSerializer

class AmistadViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Amistad.objects.all()
    serializer_class = AmistadSerializer

class NotificacionesAmistadViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Notificaciones_amistad.objects.all()
    serializer_class = NotificacionesAmistadSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated, )
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer