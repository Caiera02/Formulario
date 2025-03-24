from django.db import models

# Create your models here.

from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    criterio = models.CharField(max_length=100)
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.colaborador.nome} - {self.criterio}: {self.nota}"
