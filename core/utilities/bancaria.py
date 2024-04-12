"""Django models utilities."""

# Django
from django.db import models

class BancariaModel(models.Model):
    
    fecha_creacion = models.DateTimeField(
        'fecha creacion',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    fecha_modificacion = models.DateTimeField(
        'fecha modificacion',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'fecha_creacion'
        ordering = ['-fecha_creacion', '-fecha_modificacion']