from django.db import models
from django.contrib.auth.models import AbstractUser

# utilities
from core.utilities import BancariaModel


class UsuariosModel(BancariaModel, AbstractUser):
    """Modelo de usuario
    Extiende del User Abstract de Django, agregamos algunos campos extra.
    """

    """tipo de genero"""
    GENERO = (
        (2, 'PREFIERO NO DECIRLO'),
        (1, 'MASCULINO'),
        (0, 'FEMENINO'),
    )

    REQUIRED_FIELDS = []

    email = models.EmailField(
        verbose_name="Email",
        unique=True
    )

    """ Bandera para saber si esta logueado """
    estado_sesion = models.BooleanField(
        default=False,
        verbose_name="Estado de Sesión",
    )

    """ Bandera para saber si esta activo """
    activo = models.BooleanField(
        default=True,
        verbose_name="Estado de Usuario",
    )

    cliente = models.BooleanField(
        default=False
    )

    identificacion = models.CharField(
        max_length=20,
        verbose_name="identificacion",
        unique=True,
        blank=True,
        null=True
    )

    prefijo_telefono = models.IntegerField(
        verbose_name="Prefijo telefónico",
        blank=True,
        null=True
    )

    telefono = models.CharField(
        max_length=20,
        verbose_name="telefono",
        unique=True,
        blank=True,
        null=True
    )

    genero_usuario = models.IntegerField(
        'Genero',
        choices=GENERO,
        default=2
    )

    def __str__(self) -> str:
        return f"{self.identificacion}/{self.email}"

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta(BancariaModel.Meta):
        """Meta class."""
        db_table = "usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
