from django import forms
from formulario.models import Avaliacao

# Opções de avaliação de 1 a 5
OPCOES_AVALIACAO = [(i, str(i)) for i in range(1, 6)]



class AvaliacaoModelForm(forms.ModelForm):
    # criterio = forms.ChoiceField(choices=criterios, label="Critério")
    nota = forms.ChoiceField(choices=OPCOES_AVALIACAO, widget=forms.Select(), label="Nota")
    class Meta:
        model = Avaliacao
        fields = '__all__'


# Validação formulario
    # def clean_criterio(self):# Passando o campo que quero validar do meu formulario
    #     valor = self.cleaned_data.get('criterio')#Criando variavel e colocando o campo do formulario 'criterio'
    #     if valor != '':
    #         self.add_error('criterio','Precisa digitar teste')
    #     return valor
        