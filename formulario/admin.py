from django.contrib import admin
from formulario.models import Colaborador, Avaliacao, Criterio
# Rfrom .models import Colaboradoregister your models here.

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display=('colaborador','criterio','nota',)
 
@admin.register(Criterio)
class CriterioAdmin(admin.ModelAdmin):
    list_display=('nome',)
    
 
        
