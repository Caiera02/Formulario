from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Colaborador, Avaliacao
from .forms import AvaliacaoForm

def avaliacao_view(request):
    colaboradores = Colaborador.objects.all()
    criterios = ["Liderança", "Assiduidade", "Comprometimento", "Proatividade", "Trabalho em Equipe",
                 "Foco em Resultado", "Capacidade Analítica", "Gestão de Tempo", "Confiabilidade",
                 "Produtividade", "Qualidade", "Aptidão Técnica", "Apresentação"]

    if request.method == "POST":
        for colaborador_id in request.POST.getlist("colaborador_id"):
            colaborador = Colaborador.objects.get(id=colaborador_id)
            for criterio in criterios:
                nota = request.POST.get(f"nota_{colaborador_id}_{criterio}")
                if nota:
                    Avaliacao.objects.update_or_create(
                        colaborador=colaborador,
                        criterio=criterio,
                        defaults={"nota": int(nota)}
                    )
        return redirect(reverse('avaliacao'))

    avaliacoes = Avaliacao.objects.all()
    return render(request, "avaliacao.html", {"colaboradores": colaboradores, "criterios": criterios, "avaliacoes": avaliacoes})
