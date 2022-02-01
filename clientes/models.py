from django.db import models


class Cliente(models.Model):
    
    clienteid = models.BigAutoField(primary_key=True, verbose_name='Cliente ID')
    statuscliente = models.CharField(verbose_name='Status',
        max_length=2,
        default = '',
        choices=(
            ('A', 'Ativo'),
            ('I', 'Inativo'),
        )
        )
    pessoa = models.CharField(
        max_length=2,
        default = '',
        choices=(
            ('F', 'Fisíca'),
            ('J', 'Jurídica'),
        )
        )
    cpf = models.CharField(max_length=12, unique=True, verbose_name='CPF')
    cnpj = models.CharField(max_length=15, unique=True, verbose_name='CNPJ')
    rg = models.CharField(max_length=12, verbose_name='RG')
    ie = models.CharField(max_length=15, verbose_name='IE')
    inadimplencia = models.CharField(verbose_name='Inadimplência',
        max_length=2,
        default = '',
        choices=(
            ('S', 'Sim'),
            ('N', 'Não'),
        )
        )
    nomecliente = models.CharField(max_length=50, verbose_name='Nome Cliente/Razão Social')
    email = models.CharField(max_length=50, verbose_name='E-mail')
    datanascimento = models.DateField(verbose_name='Data de nascimento')
    cep = models.IntegerField(max_length= 20, verbose_name='CEP')
    endereco = models.CharField(max_length=50, verbose_name="Endereço")
    uf = models.CharField(verbose_name="UF",
        max_length=2,
        default = '',
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
    complemento = models.CharField(max_length=20)

    def __str__(self):
        return self.nomecliente




"""
    carroid = models.ForeignKey('Placa', on_delete=models.CASCADE)
    movimentacaodatahora = models.datetime()
    movimentacaoGPS = models.CharField(max_length=50)
    movimentacaodirecao = models.CharField(max_length=20)
    placaveiculo = models.CharField(max_length=7)
    descricaoveiculo = models.CharField(max_length=50)
    grupocarro = 
    filial = 
    descricaoveiculo = 
    monitoramentoignicao = models.BooleanField(default=False)
"""