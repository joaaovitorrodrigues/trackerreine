# from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
from veiculos.models import Veiculo


class Filial(models.Model):
    nome_filial = models.CharField(max_length=100)
    descricao_grupo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(
        default=timezone.now, verbose_name='Data de Cadastro')

    class Meta:
        verbose_name_plural = 'Filiais'
        ordering = ('nome_filial', )

    def __str__(self):
        return self.nome_filial


class Motorista(models.Model):
    nome_motorista = models.CharField(
        max_length=100, verbose_name='Nome do motorista')
    cpf_motorista = models.CharField(
        max_length=100, unique=True, verbose_name='CPF')
    rg_motorista = models.CharField(max_length=100, verbose_name='RG')
    email = models.CharField(max_length=100)

    filial = models.ForeignKey(Filial, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_motorista


class Grupoveiculo(models.Model):
    nome_grupo = models.CharField(
        max_length=100, verbose_name='Grupo de veículos')
    descricao_grupo = models.CharField(
        max_length=100, verbose_name='Descrição Grupo')
    email = models.CharField(max_length=100)

    veiculo = models.ForeignKey(
        Veiculo, verbose_name='Veiculos', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Grupo de veículos'
        ordering = ('nome_grupo', )

    def __str__(self):
        return self.nome_grupo


"""
class Local(models.Model):
    nome_cerca = models.CharField(max_length=100)
    descricao_cerca = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)"""
