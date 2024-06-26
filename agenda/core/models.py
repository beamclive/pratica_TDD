from django.db import models

class AgendaModel(models.Model):
    nome = models.CharField('Nome', max_length=150)
    telefone = models.CharField('Telefone', max_length=20)
    cpf = models.CharField('Cpf', max_length=30, default='')

    def __str__(self):
        return self.nome
