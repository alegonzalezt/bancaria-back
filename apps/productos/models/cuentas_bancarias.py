from django.db import models
from apps.usuarios.models.usuarios import UsuariosModel
from core.utilities import BancariaModel


class CuentaBancaria(BancariaModel):
    """Modelo de cuentas bancarias
    """ 

    usuario_cuenta = models.OneToOneField(
        UsuariosModel,
        on_delete=models.CASCADE, 
        verbose_name="Usuario de cuenta",
        unique=True,
    )
    
    numero_cuenta = models.CharField(
        max_length=11,
        verbose_name="Numero de cuenta",
        unique=True,
        default=0
    )
      
    saldo_cuenta = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        verbose_name="Saldo Cuenta"
    )

    """ Bandera para saber el estado de la cuenta """
    estado_cuenta = models.BooleanField(
        default=True,
        verbose_name="Estado de Cuenta",
    ) 

    def __str__(self) -> str:
        return f"{self.usuario_cuenta.identificacion}/{self.numero_cuenta}"

    class Meta(BancariaModel.Meta):
        """Meta class."""
        db_table = "cuenta_bancaria"
        verbose_name = "Cuenta Bancaria"
        verbose_name_plural = "Cuentas Bancarias"
