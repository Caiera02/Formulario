from django.contrib import admin
from openpyxl import Workbook
from django.http import HttpResponse
from datetime import date
from ra.models import Avaliacao, Criterio,Colaborador

# Register your models here.

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display =('nome',)

@admin.register(Criterio)
class CriterioAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display=('colaborador','criterio', 'nota',)
    
    #importando para excel
    def export_product_to_excel(request,self,queryset):
    # Cria o workbook e a planilha
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Avaliação R.A"

        # Adiciona o cabeçalho
        headers = ['Nome', 'Criterio','Nota',]
        worksheet.append(headers)

        # Recupera os dados do modelo e preenche a planilha
        avaliacao = Avaliacao.objects.all() #Busca Avaliação todos o objetos
        data_atual= date.today()
        
        for computers in avaliacao: #Percorre os objetos
            worksheet.append([
                str (computers.colaborador),
                str (computers.criterio),
                int (computers.nota),
            #   controle.delivery.strftime("%Y-%m-%d"),
            #   controle.delivery.strftime("%H:%M:%S"),
            ])

        # Configura a resposta HTTP para o download
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = f"attachment; filename=Avaliacao_RA_{data_atual}.xlsx"
        workbook.save(response)
        return response
    
    export_product_to_excel.short_description = 'Exportar para excel'
    actions = [export_product_to_excel]
    
    
    

    
