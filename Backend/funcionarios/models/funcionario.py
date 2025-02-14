from django.db import models

from django.contrib.auth.models import User

class Setor(models.TextChoices):
    CONTABILIDADE = 'Contabilidade', 'Contabilidade'
    FINANCEIRO = 'Finanças', 'Financeiro'
    ATENDIMENTO = 'Atendimento', 'Atendimento'
    ORCAMENTO = 'Orçamento', 'Orçamento'
    TI = 'TI' , 'TI'

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    setor = models.CharField(
        max_length=30,
        choices=Setor.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
