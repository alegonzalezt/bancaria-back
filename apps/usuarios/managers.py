from django.apps import apps
from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        """Crea y guarda un Usuario con el correo y la contraseña."""
        if not username:
            raise ValueError("El email es requerido")
        usuario = self.model(username=username, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario

    def create_user(self, username, password=None, **extra_fields):
        """Crea y guarda un Usuario estándar con el correo y la contraseña."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """Crea y guarda un Usuario con el correo y la contraseña."""
        apps.get_model("usuarios", "UsuariosModel")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser debe tener is_superuser=True.")

        return self._create_user(username, password, **extra_fields)