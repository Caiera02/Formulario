from django import forms
from formulario.models import Avaliacao

class AvaliacaoModelForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = '__all__'


#Validação formulario

    # def clean_criterio(self):# Passando o campo que quero validar do meu formulario
    #     valor = self.cleaned_data.get('criterio')#Criando variavel e colocando o campo do formulario 'criterio'
    #     if valor != '':
    #         self.add_error('criterio','Precisa digitar teste')
    #     return
    
    def clean_colaborador(self):
        data = self.cleaned_data.get('colaborador')
        if data == 'Caio Cezar':
            self.add_error('colaborador','Lindo')
        
        return data
    
        