from django.db import models

# Create your models here.

class Usuario(models.Model):

    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"]
    ]

    nome = models.CharField(max_length=20, null=False, verbose_name='Nome')
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=10)
    email = models.EmailField(null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = ' Usuários'


class SetorBanheiro(models.Moodel):
    nome = models.CharField(max_length=20, null=False, verbose_name='Nome')
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    date = models.DateField(max_length=100, verbose_name='Data',null=True, auto_now=True)

    def __str__(self):
        return self.name

class SetorLaboratorio(models.Model):
    nome = models.CharField(max_length=20, null=False, verbose_name='Nome')
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    date = models.DateField(max_length=100, verbose_name='Data',null=True, auto_now=True)

    def __str__(self):
        return self.name

class SetorSalas(models.Model):
    nome = models.CharField(max_length=20, null=False, verbose_name='Nome')
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    date = models.DateField(max_length=100, verbose_name='Data',null=True, auto_now=True)

    def __str__(self):
        return self.name

class SetorAuditorio(models.Model):
    nome = models.CharField(max_length=20, null=False, verbose_name='Nome')
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    date = models.DateField(max_length=100, verbose_name='Data',null=True, auto_now=True)
    
    def __str__(self):
        return self.name