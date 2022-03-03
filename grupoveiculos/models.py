from clientes.models import Cliente
from django.contrib.auth.models import User
from django.db import models


class Grupoveiculo(models.Model):
    nome_grupo = models.CharField(max_length=100)
    descricao_grupo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    # data_cadastro = models.DateTimeField(auto_now_add=True)
    # data_atualizacao = models.DateTimeField(auto_now=True)
    # usuario = models.ForeignKey(User, on_delete=models.PROTECT)
