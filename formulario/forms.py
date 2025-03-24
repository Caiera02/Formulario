from django import forms
from .models import Avaliacao, Colaborador

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['colaborador', 'criterio', 'nota']
