from django.db import models

class plano(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Mensalidade(models.Model):
    
    aluno = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    plano = models.ForeignKey(plano, on_delete=models.CASCADE)
    treino = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Mensalidades' 
        
    def __str__(self):
        return self.aluno 



