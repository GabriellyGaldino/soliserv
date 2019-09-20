from django.db import models

# Create your models here.

class Setor(models.Model):
    nome = models.CharField(max_length=20, null=False, verbose_name='Nome')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

class Solicitacao(models.Model):

    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    data = models.DateField(max_length=100, verbose_name='Data',null=True, auto_now=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)