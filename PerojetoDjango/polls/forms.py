from django import forms
from .models import Doenca, Epidemiologico

class DateInput(forms.DateInput):
    input_type = 'date'

class doencaForm(forms.ModelForm):
    class Meta:
        model = Doenca
        fields = ['nome', 'sintomas']

class epidemioForm(forms.ModelForm):
    class Meta:
        model = Epidemiologico
        fields = [ 'data_coleta', 'doenca_associada']
        widgets = {'data_coleta' : DateInput()}

