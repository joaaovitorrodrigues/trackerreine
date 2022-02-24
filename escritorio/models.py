from django.db import models


class Escritorio(models.Model):
    nome_escritorio = models.CharField(max_length=100)
    descricao_escritorio = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # data_cadastro = models.DateTimeField(auto_now_add=True)
    # data_atualizacao = models.DateTimeField(auto_now=True)
