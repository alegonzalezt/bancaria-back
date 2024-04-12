# django
from rest_framework import serializers

# model
from apps.usuarios.models.usuarios import UsuariosModel


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosModel
        exclude = ['fecha_creacion', 'fecha_modificacion']
