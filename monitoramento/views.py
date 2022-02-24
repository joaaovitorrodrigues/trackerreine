from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='users:login',
                redirect_field_name='next')
def monitoramento(request):
    return render(request, 'monitoramento/pages/monitoramento.html')


@login_required(login_url='users:login',
                redirect_field_name='next')
def dashboard(request):
    return render(request, 'users/pages/dashboard.html')
