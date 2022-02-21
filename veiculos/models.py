from django.db import models
from django.utils import timezone


class Veiculo(models.Model):
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

    marcaveiculo = models.CharField(verbose_name="Marca",
                                    default='',
                                    max_length=2,
                                    choices=(
                                        ('', 'Alfa Romeo'),
                                        ('', 'Asia Motors'),
                                        ('', 'Aston Martin'),
                                        ('', 'Audi'),
                                        ('', 'BMW'),
                                        ('', 'Bugre'),
                                        ('', 'Cadillac'),
                                        ('', 'Caoa Cherry'),
                                        ('', 'Chrysler'),
                                        ('', 'Citroen'),
                                        ('', 'Cross Lander'),
                                        ('', 'Dodge'),
                                        ('', 'FIAT'),
                                        ('', 'FORD'),
                                        ('', 'GM - Chevrolet'),
                                        ('', 'Honda'),
                                        ('', 'Hyundai'),
                                        ('', 'IVECO'),
                                        ('', 'JAC'),
                                        ('', 'Jaguar'),
                                        ('', 'JEEP'),
                                        ('', 'KIA Motors'),
                                        ('', 'Mercedes-Benz'),
                                        ('', 'Mitsubishi'),
                                        ('', 'Nissan'),
                                        ('', 'Peugeot'),
                                        ('', 'Renault'),
                                        ('', 'Suzuki'),
                                        ('', 'Toyota'),
                                        ('', 'Volvo'),
                                        ('', 'Volkswagem'),
                                    )
                                    )
    modelo = models.CharField(max_length=15, verbose_name="Modelo")
    cor = models.CharField(max_length=10, verbose_name="Cor")
    chassi = models.CharField(max_length=15, verbose_name="Chassi")
    renavam = models.IntegerField(verbose_name="Renavam")
    localinstalacao = models.CharField(
        max_length=50, verbose_name="Local da Instalação", default='')
    data_cadastro = models.DateTimeField(
        default=timezone.now, verbose_name="Data de Cadastro")
