from django.db import models
from django.conf import settings

# Create your models here.

# ----------------------
# App: pacientes/models.py
# ----------------------

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)

    run = models.CharField(max_length=15, db_index=True)
    dv = models.CharField(max_length=1)

    inmigrante = models.BooleanField(default=False)
    nacionalidad = models.CharField(max_length=100)
    pueblo_originario = models.BooleanField(default=False)
    edad = models.IntegerField()
    discapacidad = models.BooleanField(default=False)
    privada_libertad = models.BooleanField(default=False)
    trans_masculino = models.BooleanField(default=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Paciente"
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        indexes = [
            models.Index(fields=['run'], name='idx_paciente_run'),
            models.Index(fields=['apellido_paterno'], name='idx_paciente_apellido'),
        ]

    def __str__(self):
        return self.nombre_completo()

    def nombre_completo(self):
        parts = [self.nombre, self.apellido_paterno]
        if self.apellido_materno:
            parts.append(self.apellido_materno)
        return " ".join(parts)


class Hospitalizacion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="hospitalizaciones")
    fecha_ingreso = models.DateField()
    fecha_alta = models.DateField()
    motivo = models.CharField(max_length=200, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Hospitalizacion"
        verbose_name = "Hospitalización"
        verbose_name_plural = "Hospitalizaciones"
        indexes = [
            models.Index(fields=['paciente', 'fecha_ingreso'], name='idx_hosp_paciente_fecha'),
        ]

    def __str__(self):
        return f"Hospitalización {self.id} - {self.paciente.nombre_completo()}"
    
    from django.db import models
from django.conf import settings