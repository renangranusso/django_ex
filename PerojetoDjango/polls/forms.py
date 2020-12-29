from django import forms
from .models import Doenca

class doencaForm(forms.ModelForm):
    class Meta:
        model = Doenca
        fields = ['nome', 'sintomas']