

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm


@login_required(login_url='users:login',
                redirect_field_name='next')
def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'users/pages/register_view.html', {
        'form': form,
        'form_action': reverse('users:register_create'),
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
        return redirect(reverse('users:login'))

    return redirect('users:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'users/pages/login.html', {
        'form': form,
        'form_action': reverse('users:login_create')
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Você está logado.')
            login(request, authenticated_user)
        else:
            messages.error(
                request, 'Credenciais inválidas.')
    else:
        messages.error(request, 'Usuário ou senha inválidos.')

    return redirect(reverse('users:dashboard'))

# Usuario logado


@login_required(login_url='users:login',
                redirect_field_name='next')
def logout_view(request):
    # Proteção: O usuario deve estar logado, ser um POST
    if not request.POST:
        # Se não, retorna para o login
        return redirect(reverse('users:login'))
    # Proteção: O usuario deve estar logado, verificação de username
    if request.POST.get('username') != request.user.username:
        # Se não, retorna para o login
        return redirect(reverse('users:login'))

    logout(request)
    return redirect(reverse('users:login'))


@login_required(login_url='users:login',
                redirect_field_name='next')
def dashboard(request):
    return render(request, 'users/pages/dashboard.html')
