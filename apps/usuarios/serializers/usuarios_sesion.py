# django
from django.contrib.auth import authenticate

# modelos
from rest_framework.authtoken.models import Token
from apps.usuarios.models.usuarios import UsuariosModel

# serialzers
from rest_framework import serializers


def generos_usuario(id_genero):
    genero = [
        {"id": 2, "nombre": "PREFIERO NO DECIRLO"},
        {"id": 1, "nombre": "MASCULINO"},
        {"id": 0, "nombre": "FEMENINO"},
    ]
    for x in genero:
        if x["id"] == id_genero:
            return x["nombre"]

    return genero[0]['nombre']


class UsuarioSesionSerializer(serializers.Serializer):
    """Serializador para Usuario Sesion.
    Maneja la información de inicio de sesión.
    """

    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=5, max_length=64, write_only=True)
    nombres = serializers.CharField(read_only=True)
    identificacion = serializers.CharField(read_only=True)
    genero_usuario = serializers.CharField(read_only=True)
    estado_sesion = serializers.BooleanField(read_only=True)
    activo = serializers.BooleanField(read_only=True)
    fecha_creacion = serializers.DateTimeField(read_only=True)
    cliente = serializers.BooleanField(read_only=True)
    permisos = serializers.ListField(read_only=True)

    def validate(self, data):
        """Valida credenciales."""
        usuario = authenticate(username=data["username"], password=data["password"])

        if usuario:
            usuario_i = UsuariosModel.objects.get(username=data["username"])
        else:
            raise serializers.ValidationError("Credenciales inválidas.")

        if not usuario_i.activo:
            raise serializers.ValidationError("Cuenta inactiva.")

        self.context["usuario"] = usuario
        return data

    def create(self, data):
        """Crea un nuevo token unico usuario."""
        usuario = self.context["usuario"]
        usuario.estado_sesion = True
        usuario.save()
        token, created = Token.objects.get_or_create(user=usuario)

        # traemos el usuario y los permisos
        permisos = usuario.get_all_permissions()

        genero_usuario = generos_usuario(usuario.genero_usuario)

        datos_usuario = {
            "id": usuario.id,
            "email": usuario.email,
            "username": usuario.username,
            "nombres": usuario.get_full_name(),
            "identificacion": usuario.identificacion,
            "genero_usuario": genero_usuario,
            "cliente": usuario.cliente,
            "estado_sesion": usuario.estado_sesion,
            "activo": usuario.activo,
            "fecha_creacion": usuario.fecha_creacion,
            "permisos": permisos
        }
        return datos_usuario, token.key
