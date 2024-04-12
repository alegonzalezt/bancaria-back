# django
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response

# serializers
from apps.usuarios.serializers.usuarios_sesion import UsuarioSesionSerializer

# model
from apps.usuarios.models.usuarios import UsuariosModel

# permisos
from rest_framework.permissions import AllowAny, IsAuthenticated


class UsuariosSesionViews(viewsets.GenericViewSet):

    serializer_class = UsuarioSesionSerializer

    def get_permissions(self):
        """
        Asignacion de permisos por accion
        """
        if self.action in ['inicio_sesion', 'cierre_sesion']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=["post"], url_path="iniciar-sesion")
    def inicio_sesion(self, request):
        """
        Inicio de sesión
        """
        datos = {}
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            usuario, token = serializer.save()

            datos = {"usuario": UsuarioSesionSerializer(usuario).data, "token": token}

            return Response(datos, status=status.HTTP_200_OK)

        except:
            datos = {"mensaje": "Error al iniciar sesión."}
            return Response(datos, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], url_path="cierre-sesion")
    def cierre_sesion(self, request):
        """
        Cierre de sesión
        """
        datos = {}

        try:
            usuario_peticion = request.user
            usuario = UsuariosModel.objects.get(id=usuario_peticion.id)
            usuario.estado_sesion = False
            usuario.save()

            datos = {"mensaje": "Sesión Finalizada", "estado_sesion": usuario.estado_sesion}

            return Response(datos, status=status.HTTP_200_OK)
        except:
            datos = {"mensaje": "Error al Finalizar sesión"}

            return Response(datos, status=status.HTTP_200_OK)