from django.urls import path, include
from rest_framework import routers

# views
from apps.usuarios.views.usuarios import UsuariosViews
from apps.usuarios.views.usuarios_sesion import UsuariosSesionViews

app_name = 'usuarios'
router = routers.DefaultRouter()
router.register('usuarios-registro', UsuariosViews, basename="usuarios-registro")
router.register('usuarios-sesion', UsuariosSesionViews, basename="usuarios-sesion")

urlpatterns = [
    path('', include(router.urls)),
]