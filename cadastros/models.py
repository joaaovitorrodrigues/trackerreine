# from django.contrib.auth.models import User
from django.db import models


class Filial(models.Model):
    nome_filial = models.CharField(max_length=100)
    descricao_grupo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Motorista(models.Model):
    nome_motorista = models.CharField(max_length=100)
    cpf_motorista = models.CharField(max_length=100)
    rg_motorista = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


"""
class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)"""
