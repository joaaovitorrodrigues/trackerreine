import json

import requests


def consulta_cep(cep):
    cep_digitado = cep
    request = requests.get(
        'https://viacep.com.br/ws/{}/json/'.format(cep_digitado))
    dados = request.json()
