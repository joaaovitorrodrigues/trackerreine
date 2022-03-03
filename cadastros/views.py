from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='users:login',
                redirect_field_name='next')
def cadastro(request):
    return render(request, 'cadastros/pages/cadastros.html')


@login_required(login_url='users:login',
                redirect_field_name='next')
def filial(request):
    return render(request, 'cadastros/pages/filial.html')


@login_required(login_url='users:login',
                redirect_field_name='next')
def motorista(request):
    return render(request, 'cadastros/pages/motoristas.html')


@login_required(login_url='users:login',
                redirect_field_name='next')
def cerca(request):
    return render(request, 'cadastros/pages/cercas.html')


@login_required(login_url='users:login',
                redirect_field_name='next')
def dashboard(request):
    return render(request, 'users/pages/dashboard.html')
