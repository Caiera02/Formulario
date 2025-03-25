from django.contrib import admin
from .models import Colaborador, Avaliacao
# Rfrom .models import Colaboradoregister your models here.

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display=(Colaborador,)

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display=('colaborador','criterio','nota',)


        
