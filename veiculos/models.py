from clientes.models import Cliente
from django.db import models
from django.utils import timezone


class Veiculo(models.Model):
    marca_veiculo = (
        ('A', 'Alfa Romeo'),
        ('A', 'Asia Motors'),
        ('A', 'Aston Martin'),
        ('A', 'Audi'),
        ('B', 'BMW'),
        ('B', 'Bugre'),
        ('C', 'Cadillac'),
        ('C', 'Caoa Cherry'),
        ('C', 'Chrysler'),
        ('C', 'Citroen'),
        ('C', 'Cross Lander'),
        ('D', 'Dodge'),
        ('F', 'FIAT'),
        ('F', 'FORD'),
        ('G', 'GM - Chevrolet'),
        ('H', 'Honda'),
        ('H', 'Hyundai'),
        ('I', 'IVECO'),
        ('J', 'JAC'),
        ('J', 'Jaguar'),
        ('J', 'JEEP'),
        ('K', 'KIA Motors'),
        ('M', 'Mercedes-Benz'),
        ('M', 'Mitsubishi'),
        ('N', 'Nissan'),
        ('P', 'Peugeot'),
        ('R', 'Renault'),
        ('S', 'Suzuki'),
        ('T', 'Toyota'),
        ('V', 'Volvo'),
        ('V', 'Volkswagem'),
    )

    veiculoid = models.BigAutoField(
        primary_key=True, verbose_name="Veiculo ID")
    statusveiculo = models.CharField(verbose_name="Status",
                                     max_length=2,
                                     default='',
                                     choices=(
                                         ('A', 'Ativo'),
                                         ('I', 'Inativo'),
                                         ('E', 'Espera'),
                                     )
                                     )
    placaveiculo = models.CharField(verbose_name="Placa", max_length=10)
    ano_fab = models.IntegerField(verbose_name="Ano Fabricação")
    ano_mod = models.IntegerField(verbose_name="Ano Modelo")
    tipoveiculo = models.CharField(verbose_name="Tipo",
                                   max_length=2,
                                   choices=(
                                       ('CM', 'Caminhão'),
                                       ('CA', 'Carro'),
                                       ('LA', 'Lancha'),
                                       ('MO', 'Moto'),
                                       ('PU', 'PickUp'),
                                       ('TR', 'Trator'),
                                       ('VA', 'Van'),
                                   )
                                   )

    marcaveiculo = models.CharField(
        max_length=15, choices=marca_veiculo, null=False)
    modelo = models.CharField(max_length=15, verbose_name="Modelo")
    cor = models.CharField(max_length=10, verbose_name="Cor")
    chassi = models.CharField(max_length=15, verbose_name="Chassi")
    renavam = models.IntegerField(verbose_name="Renavam")
    localinstalacao = models.CharField(
        max_length=50, verbose_name="Local da Instalação", default='')
    data_cadastro = models.DateTimeField(
        default=timezone.now, verbose_name="Data de Cadastro")

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
