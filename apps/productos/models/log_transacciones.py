from django.db import models
from core.utilities import BancariaModel
import jsonfield
from apps.productos.models.cuentas_bancarias import CuentaBancaria


class LogsTransacciones(BancariaModel):
    """
    Logs de transacciones para operaciones de cuentas
    """
    referencia_cuenta = models.ForeignKey(
        CuentaBancaria,
        verbose_name="Referencia Cuenta Bancaria",
        on_delete=models.CASCADE
    )
    descripcion_log = jsonfield.JSONField()

    def __str__(self) -> str:
        return f"#{self.referencia_cuenta.numero_cuenta}"

    class Meta(BancariaModel.Meta):
        """Meta class."""
        db_table = 'logs_trans_cuenta_bancaria'
        verbose_name = 'Log Transacción'
        verbose_name_plural = 'Logs Transacciones'