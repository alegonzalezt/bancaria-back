# drf
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

# serializers
from apps.usuarios.serializers.usuarios import UsuariosSerializer


class UsuarioRegistroSerializer(serializers.Serializer):
    usuario = UsuariosSerializer(many=False)

    def create(self, validated_data):
        usuario_peticion = validated_data.get("usuario")
        usuario_peticion["password"] = make_password(usuario_peticion["password"])
        usuario_serializer = UsuariosSerializer(data=usuario_peticion)
        usuario_serializer.is_valid(raise_exception=True)
        usuario_i = usuario_serializer.save()

        return {"usuario": usuario_i}
