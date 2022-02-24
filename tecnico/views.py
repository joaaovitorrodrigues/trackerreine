
from django.shortcuts import render


def tecnicos(request):
    return render(request, 'tecnico/pages/tecnico.html')
