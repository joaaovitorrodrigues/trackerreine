from django.http import HttpResponse
from django.shortcuts import render


def clientes(request):
    return render(request, 'clientes/pages/cliente.html')
