"""
from django.db import models


class Monitoramento(models.Model):
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    nomecliente = models.ForeignKey()  # Herdado do models users
    placaveiculo = models.ForeignKey()  # Herdado do models veiculos
    odometro = models.CharField(max_length=50)
    datagps = models.DateTimeField()
    datasis = models.DateTimeField()
    ignicao = models.BooleanField(default=False)
    velocidade = models.BooleanField(default=0)
    latidude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)"""
