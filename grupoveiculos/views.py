from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from grupoveiculos.forms import GrupoveiculoForm

from .models import Grupoveiculo


def grupoveiculo(request):
    grupoveiculos = Grupoveiculo.objects.all()
    register_form_data = request.session.get('register_form_data', None)
    form = GrupoveiculoForm(register_form_data)
    return render(request, 'grupoveiculos/pages/grupoveiculos.html', {
        'grupoveiculos': grupoveiculos,
        'form': form,
        'form_action': reverse('grupoveiculo:grupoveiculos_add'),
    })
    """# Pega os objetos do banco (grupoveiculos)
    grupoveiculos = Grupoveiculo.objects.all()

    return render(request, 'grupoveiculos/pages/grupoveiculos.html',
                  {'grupoveiculos': grupoveiculos})"""


def grupoveiculos_add(request):
    if request.method == "POST":
        form = GrupoveiculoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Seu usuário foi criado, por favor, faça o login.')
        return redirect('../')

    # Cria o formulário
    form = GrupoveiculoForm()
    return render(request, 'grupoveiculos/pages/grupoveiculos_add.html',
                  {'form': form})

    """if request.POST:
        if form.is_valid():
            form.save()
            return redirect('gruposveiculos')

    # Renderiza no template
    return render(request, 'grupoveiculos/pages/grupoveiculos_add.html',
                  {
                      'form': form
                  })"""


def grupoveiculo_edit(request, id):

    context = {}

    obj = get_object_or_404(GrupoveiculoForm, id=id)

    form = GrupoveiculoForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('../')

    context['form'] = form

    return render(request, 'grupoveiculos/pages/grupoveiculos_edit.html',
                  context)
