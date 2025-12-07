# pacientes/forms.py
from django import forms
from .models import Paciente
from utils.validators import validar_rut_chileno  # Validador de RUT chileno

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            "nombre",
            "apellido_paterno",
            "apellido_materno",
            "run",
            "dv",
            "edad",
            "nacionalidad",
            "inmigrante",
            "pueblo_originario",
            "discapacidad",
            "privada_libertad",
            "trans_masculino",
        ]

        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre"}),
            "apellido_paterno": forms.TextInput(attrs={"placeholder": "Apellido paterno"}),
            "apellido_materno": forms.TextInput(attrs={"placeholder": "Apellido materno"}),
            "run": forms.NumberInput(attrs={"placeholder": "RUN (8 dígitos sin DV)"}),
            "dv": forms.TextInput(attrs={
                "placeholder": "DV",
                "maxlength": "1",
                "style": "text-transform:uppercase;"
            }),
            "edad": forms.NumberInput(attrs={"placeholder": "Edad"}),
            "nacionalidad": forms.TextInput(attrs={"placeholder": "Nacionalidad"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        run = cleaned_data.get("run")
        dv = cleaned_data.get("dv")
        if run and dv:
            try:
                # Validación RUT chileno (8 dígitos + DV)
                validar_rut_chileno(run, dv)
            except forms.ValidationError as e:
                # Mostrar error en el campo DV
                self.add_error("dv", e)
        return cleaned_data

    def clean_run(self):
        run = self.cleaned_data.get("run")
        if not run:
            return run

        # Verificar duplicados en la base de datos
        qs = Paciente.objects.filter(run=run)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("⚠️ Este RUT ya está registrado.")
        return run
