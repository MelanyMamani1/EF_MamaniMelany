from django import forms
from .models import Mamani_Persona

class MamaniPersonaForm(forms.ModelForm):
    class Meta:
        model = Mamani_Persona
        fields = ['nombre', 'apellidos', 'sexo']
        widgets = {
            'sexo': forms.Select(choices=Mamani_Persona.SEXO_CHOICES),
        }
