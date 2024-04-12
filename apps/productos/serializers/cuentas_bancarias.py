from rest_framework import serializers
from apps.productos.models.cuentas_bancarias import CuentaBancaria
from apps.usuarios.models.usuarios import UsuariosModel
import random

def generar_numero_cuenta():
    numero_cuenta = random.randint(10000000000, 99999999999)
    return str(numero_cuenta)


class UsuarioCuentaSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.SerializerMethodField()

    def get_nombre_completo(self, obj):
        nombre_usuario = None
        if obj:
            nombre_usuario = obj.get_full_name()
        return nombre_usuario
        
    class Meta:
        model = UsuariosModel
        fields = (
            "id",
            "nombre_completo",
        )


class CuentaBancariaSerializer(serializers.ModelSerializer):
    usuario = serializers.SerializerMethodField()

    def get_usuario(self, obj):
        data_usuario = {}
        if obj.usuario_cuenta:
            serializer_i = UsuarioCuentaSerializer(obj.usuario_cuenta, many=False)
            data_usuario = serializer_i.data
        return data_usuario
    
    def create(self, validated_data):
        cuenta_bancaria = validated_data
        cuenta_bancaria["numero_cuenta"] = generar_numero_cuenta()
        return super().create(cuenta_bancaria)
      
    class Meta:
        model = CuentaBancaria
        fields = (
            'id',
            'usuario_cuenta',
            'usuario',
            'numero_cuenta',
            'saldo_cuenta',
            'estado_cuenta',
            'fecha_creacion',
        )
