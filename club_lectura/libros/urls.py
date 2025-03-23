from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResenaViewSet, AurtorViewSet,GeneroViewSet,SagaViewSet,LibroViewSet,EstadoLibroViewSet,LibroUsuarioViewSet,LibroGrupoViewSet

router = DefaultRouter()
router.register(r'resenas', ResenaViewSet)
router.register(r'autores', AurtorViewSet)
router.register(r'generos', GeneroViewSet)  
router.register(r'sagas', SagaViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'estados_libro', EstadoLibroViewSet)
router.register(r'libros_usuario', LibroUsuarioViewSet)
router.register(r'libros_grupo', LibroGrupoViewSet)






urlpatterns = [
    path('', include(router.urls)),
]
