from django.contrib import admin

#models
from apps.productos.models.cuentas_bancarias import CuentaBancaria
from apps.productos.models.log_transacciones import LogsTransacciones


@admin.register(CuentaBancaria)
class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario_cuenta',
        'numero_cuenta',
        'saldo_cuenta',
        'estado_cuenta',
    )

    search_fields = ['id', 'usuario_cuenta__identificacion']
    raw_id_fields = ['usuario_cuenta']


@admin.register(LogsTransacciones)
class LogsTransaccionesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'referencia_cuenta',
    )

    search_fields = ['id', 'referencia_cuenta__numero_cuenta']
