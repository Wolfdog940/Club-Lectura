from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Detalle_usuario, Amistad, Notificaciones_amistad, Grupo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','is_active']


class DetalleUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_usuario
        fields = '__all__'

class AmistadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amistad
        fields = '__all__'

class NotificacionesAmistadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones_amistad
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'
