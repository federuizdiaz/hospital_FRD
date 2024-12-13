# urgencias/forms.py

from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'dni', 'edad', 'obra_social']
