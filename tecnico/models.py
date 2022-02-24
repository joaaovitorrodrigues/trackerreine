"""import re

from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from utils.validacnpj import valida_cnpj
from utils.validacpf import valida_cpf


class Tecnico(models.Model):

    tecnicoid = models.BigAutoField(
        primary_key=True, verbose_name='Tecnico ID')
    statustecnico = models.CharField(verbose_name='Status',
                                     max_length=2,
                                     default='',
                                     choices=(
                                         ('A', 'Ativo'),
                                         ('I', 'Inativo'),
                                     )
                                     )
    pessoa = models.CharField(
        max_length=2,
        default='',
        choices=(
            ('F', 'Fisíca'),
            ('J', 'Jurídica'),
        )
    )
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    cnpj = models.CharField(max_length=15, unique=True, verbose_name='CNPJ')
"""
