
from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'users/pages/register_view.html', {
        'form': form,
        'form_action': reverse('users:create'),
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(
            request, 'Seu usuário foi criado, por favor, faça o login.')

        del(request.session['register_form_data'])

    return redirect('users:register')


"""def usuarios(request):
    request.session['number'] = request.session.get('number')
    request.session['number'] += 1

    form = RegisterForm()
    return render(request, 'users/pages/register_view.html', {
        'form': form,
    })"""
