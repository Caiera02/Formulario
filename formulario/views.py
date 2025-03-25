from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Colaborador, Avaliacao
from django.db import transaction
from .forms import AvaliacaoForm

def avaliacao_view(request):
    form = AvaliacaoForm()
    
    colaboradores = Colaborador.objects.all()
    criterios = ["Liderança", "Assiduidade", "Comprometimento", "Proatividade", "Trabalho em Equipe",
                 "Foco em Resultado", "Capacidade Analítica", "Gestão de Tempo", "Confiabilidade",
                 "Produtividade", "Qualidade", "Aptidão Técnica", "Apresentação"]

    if request.method == "POST":
        print(request.POST)
        with transaction.atomic():  # Garante que tudo será salvo antes de continuar
            for colaborador_id in request.POST.getlist("colaborador_id"):
                colaborador = Colaborador.objects.get(id=colaborador_id)
                for criterio in criterios:
                    nota = request.POST.get(f"nota_{colaborador_id}_{criterio}")
                    
                    if nota is not None and nota.strip() != "":
                        nota = int(nota)  # Converte para inteiro apenas se não estiver vazia
                        avaliacao, created = Avaliacao.objects.update_or_create(
                            colaborador=colaborador,
                            criterio=criterio,
                            defaults={"nota": nota}
                        )
                    print(f"✔️ Avaliação salva: {avaliacao}, Criado: {created}")  # Log de salvamento
                else:
                    print(f"⚠️ Nota ausente para {colaborador.nome} - {criterio}")  # Log de erro
                    
        return redirect(reverse('avaliacao'))


    avaliacoes = Avaliacao.objects.all()
    return render(request, "avaliacao.html", {"colaboradores": colaboradores, "criterios": criterios, "avaliacoes": avaliacoes})
