from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, DetalleUsuarioViewSet, AmistadViewSet, NotificacionesAmistadViewSet, GrupoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'detalle_usuario', DetalleUsuarioViewSet, basename='detalleusuario')
router.register(r'amistad', AmistadViewSet)
router.register(r'notificaciones_amistad', NotificacionesAmistadViewSet)
router.register(r'grupo', GrupoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
