from django.shortcuts import render
from django.http import HttpResponse

def cliente(request):
    return render(request, 'clientes/pages/cliente.html')