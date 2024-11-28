from django.db import models
from django.utils.translation import gettext_lazy as _

class Todo(models.Model):
    class EstadoChoice(models.TextChoices):
        PENDIENTE = "PENDIENTE", _("PENDIENTE")
        PROCESO = "PROCESO", _("PROCESO")
        COMPLETADA = "COMPLETADA", _("COMPLETADA")
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.CharField(
        max_length=255,
        choices=EstadoChoice,
        default=EstadoChoice.PENDIENTE,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'public\".\"todo'
        ordering = ['-fecha_actualizacion']
        get_latest_by = '-fecha_actualizacion'

        