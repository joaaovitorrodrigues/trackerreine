from django.shortcuts import render


def veiculos(request):
    return render(request, 'veiculos/pages/veiculos.html')
