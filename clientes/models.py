import re

from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from utils.validacnpj import valida_cnpj
from utils.validacpf import valida_cpf


class Cliente(models.Model):

    clienteid = models.BigAutoField(
        primary_key=True, verbose_name='Cliente ID')
    statuscliente = models.CharField(verbose_name='Status',
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
    rg = models.CharField(max_length=12, verbose_name='RG')
    ie = models.CharField(max_length=15, verbose_name='IE')
    inadimplencia = models.CharField(verbose_name='Inadimplência',
                                     max_length=2,
                                     default='',
                                     choices=(
                                         ('S', 'Sim'),
                                         ('N', 'Não'),
                                     )
                                     )
    nomecliente = models.CharField(
        max_length=50, verbose_name='Nome Cliente/Razão Social')
    email = models.CharField(max_length=50, verbose_name='E-mail')
    datanascimento = models.DateField(verbose_name='Data de nascimento')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    endereco = models.CharField(max_length=50, verbose_name="Endereço")
    uf = models.CharField(verbose_name="UF",
                          max_length=2,
                          default='',
                          choices=(
                              ('AC', 'Acre'),
                              ('AL', 'Alagoas'),
                              ('AP', 'Amapá'),
                              ('AM', 'Amazonas'),
                              ('BA', 'Bahia'),
                              ('CE', 'Ceará'),
                              ('DF', 'Distrito Federal'),
                              ('ES', 'Espirito Santo'),
                              ('GO', 'Goiás'),
                              ('MA', 'Maranhão'),
                              ('MT', 'Mato Grosso'),
                              ('MS', 'Mato Grosso do Sul'),
                              ('MG', 'Minas Gerais'),
                              ('PA', 'Pará'),
                              ('PB', 'Paraíba'),
                              ('PR', 'Paraná'),
                              ('PE', 'Pernambuco'),
                              ('PI', 'Piauí'),
                              ('RJ', 'Rio de Janeiro'),
                              ('RN', 'Rio Grande do Norte'),
                              ('RS', 'Rio Grande do Sul'),
                              ('RO', 'Rondônia'),
                              ('RR', 'Roraíma'),
                              ('SC', 'Santa Catarina'),
                              ('SP', 'São Paulo'),
                              ('SE', 'Sergipe'),
                              ('TO', 'Tocantins'),
                          )
                          )
    cidade = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    complemento = models.CharField(max_length=30)
    mensalidade = models.CharField(
        max_length=10, default='R$ ', verbose_name="Mensalidade")
    vencimento = models.CharField(
        max_length=2, verbose_name="Vencimento")
    plano = models.CharField(verbose_name="Plano",
                             max_length=2,
                             choices=(
                                 ('F', 'FIT'),
                                 ('S', 'STANDARD'),
                                 ('P', 'PRIME'),
                             )
                             )
    data_cadastro = models.DateTimeField(
        default=timezone.now, verbose_name='Data de Cadastro')

    def __str__(self):
        return self.nomecliente

    def clean(self):
        error_messages = {}

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido!'

        if not valida_cnpj(self.cnpj):
            error_messages['cnpj'] = 'Digite um CNPJ válido!'

        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'Digite um CEP válido!'

        if error_messages:
            raise ValidationError(error_messages)
