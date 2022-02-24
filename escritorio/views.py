from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from escritorio.forms import EscritorioForm

from .models import Escritorio


@login_required(login_url='users:login',
                redirect_field_name='next')
def escritorios(request):
    escritorios = Escritorio.objects.all()
    register_form_data = request.session.get('register_form_data', None)
    form = EscritorioForm(register_form_data)
    return render(request, 'escritorio/pages/escritorio.html', {
        'escritorio': escritorios,
        'form': form,
        'form_action': reverse('escritorio:escritorio_add'),
    })


@login_required(login_url='users:login',
                redirect_field_name='next')
def escritorio_add(request):
    if request.method == "POST":
        form = EscritorioForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Seu usuário foi criado, por favor, faça o login.')
        return redirect('../')

    # Cria o formulário
    form = EscritorioForm()
    return render(request, 'escritorio/pages/escritorio_add.html',
                  {'form': form})


@login_required(login_url='users:login',
                redirect_field_name='next')
def escritorio_edit(request, id):
    escritorio = get_object_or_404(Escritorio, id=id)
    form = EscritorioForm(request.POST or None, instance=escritorio)

    if form.is_valid():
        form.save()
        return redirect('escritorios')

    return render(request, 'escritorio/pages/escritorio_add.html',
                  {'form': form, 'escritorio': escritorio})


@login_required(login_url='users:login',
                redirect_field_name='next')
def dashboard(request):
    return render(request, 'users/pages/dashboard.html')
