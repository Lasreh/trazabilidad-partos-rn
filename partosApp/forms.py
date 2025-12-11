from django import forms
from .models import Parto, Examenes, Patologia, Procedimiento, Anestesia, Apego, Profesionales, OtrosDatos


class PartoForm(forms.ModelForm):
    class Meta:
        model = Parto
        fields = "__all__"
        exclude = ["created_by", "updated_at", "created_at"]


class ExamenesForm(forms.ModelForm):
    class Meta:
        model = Examenes
        fields = "__all__"
        exclude = ["parto", "created_by", "created_at", "updated_at"]


class PatologiaForm(forms.ModelForm):
    class Meta:
        model = Patologia
        fields = "__all__"
        exclude = ["parto", "created_by", "created_at", "updated_at"]


class ProcedimientoForm(forms.ModelForm):
    class Meta:
        model = Procedimiento
        fields = "__all__"
        exclude = ["parto", "created_by", "created_at", "updated_at"]


class AnestesiaForm(forms.ModelForm):
    class Meta:
        model = Anestesia
        fields = "__all__"
        exclude = ["parto", "created_by", "created_at", "updated_at"]


class ApegoForm(forms.ModelForm):
    class Meta:
        model = Apego
        fields = "__all__"
        exclude = ["parto", "created_by", "created_at", "updated_at"]


class ProfesionalesForm(forms.ModelForm):
    class Meta:
        model = Profesionales
        fields = "__all__"
        exclude = ["parto", "created_by", "created_at", "updated_at"]


class OtrosDatosForm(forms.ModelForm):
    class Meta:
        model = OtrosDatos
        fields = "__all__"
        exclude = ["parto", "created_by", "created_at", "updated_at"]
