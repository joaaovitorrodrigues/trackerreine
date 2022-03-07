from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from grupoveiculos.forms import GrupoveiculoForm

from .models import Grupoveiculo


@login_required(login_url='users:login',
                redirect_field_name='next')
def grupoveiculo(request):
    grupoveiculos = Grupoveiculo.objects.all()

    context = {
        'grupoveiculos': grupoveiculos
    }
    return render(request,
                  'grupoveiculos/pages/grupoveiculos.html', context)

    def get_queryset(self):
        self.object_list = Grupoveiculo.objects.filter(username=self.user)
        return self.object_list

    """grupoveiculos = Grupoveiculo.objects.all()
    register_form_data = request.session.get('register_form_data', None)
    form = GrupoveiculoForm(register_form_data)
    return render(request, 'grupoveiculos/pages/grupoveiculos.html', {
        'grupoveiculos': grupoveiculos,
        'form': form,
        'form_action': reverse('grupoveiculo:grupoveiculos_add'),
    })
    # Pega os objetos do banco (grupoveiculos)
    grupoveiculos = Grupoveiculo.objects.all()

    return render(request, 'grupoveiculos/pages/grupoveiculos.html',
                  {'grupoveiculos': grupoveiculos})"""


@login_required(login_url='users:login',
                redirect_field_name='next')
def grupoveiculos_add(request):
    form = GrupoveiculoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('grupoveiculo:grupoveiculos')

    context = {
        'form': form
    }

    return render(request, 'grupoveiculos/pages/grupoveiculos_add.html',
                  context)


@login_required(login_url='users:login',
                redirect_field_name='next')
def grupoveiculo_edit(request, id):
    grupoveiculo = Grupoveiculo.objects.get(pk=id)

    form = GrupoveiculoForm(request.POST or None, instance=grupoveiculo)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('grupoveiculo:grupoveiculos')

    context = {
        'form': form,
    }

    return render(request, 'grupoveiculos/pages/grupoveiculos_edit.html', context)


@login_required(login_url='users:login',
                redirect_field_name='next')
def dashboard(request):
    return render(request, 'users/pages/dashboard.html')
