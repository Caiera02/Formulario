from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name= 'Colaborador'
        
    def __str__(self):
        return self.nome

class Criterio(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    criterio = models.ForeignKey(Criterio,on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])# Fazer aparecer apenas de 1 a 5
    
    class Meta:
        unique_together = ('colaborador', 'criterio') 

