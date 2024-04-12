# django
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response

# serializers
from apps.usuarios.serializers.usuarios_registro import UsuarioRegistroSerializer

# permisos
from rest_framework.permissions import AllowAny, IsAuthenticated


class UsuariosViews(viewsets.GenericViewSet):

    serializer_class = UsuarioRegistroSerializer

    def get_permissions(self):
        """
        Asignacion de permisos por accion
        """
        if self.action in ['create']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def create(self, request):
        try:
            serializer = self.get_serializer(data=self.request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
