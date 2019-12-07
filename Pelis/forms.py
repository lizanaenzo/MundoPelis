from django import forms
from .models import DatosPersona

class DatosPersonaForm(forms.ModelForm):
    class Meta:
        model = DatosPersona
        fields= [
            'nombres',
            'apellidos',
            'direccion',
            'email',
            'mensaje',
        ]