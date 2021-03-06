"""Django models utilities."""


#Django
from django.db import models


class HelpTutorModel(models.Model):
    """HelpTutorModel base model for all app models."""

    is_active = models.BooleanField(default=True, verbose_name='¿Es activo?')
    date_record = models.DateField(auto_now_add=True, verbose_name='Fecha de registro')
    date_update = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        """Meta options."""
        abstract = True

        get_latest_by = 'date_record'
        ordering = ['-date_record', '-date_update']