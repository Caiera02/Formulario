from django.shortcuts import render, redirect
from formulario.forms import AvaliacaoModelForm
from formulario.models import Criterio, Colaborador, Avaliacao

def avaliacao_view(request):
    
    if request.method == 'POST':
        new_formulario = AvaliacaoModelForm(request.POST) #criar e armazenar o que está vindo do formulario
        if new_formulario.is_valid():
                new_formulario.save()
                return redirect('new_avaliacao')
        print(new_formulario.data)
    else:
        new_formulario = AvaliacaoModelForm()

    return render(request,
                  'avaliacao.html',
                  { 'new_formulario' : new_formulario,
                   } )