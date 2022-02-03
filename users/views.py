
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import Http404

from .forms import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'users/pages/register_view.html',{
        'form': form,
    })



def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    return redirect('users:register')





    """
def usuarios(request):
    
    request.session['number'] = request.session.get('number')
    request.session['number'] += 1

    form = RegisterForm()
    return render(request, 'users/pages/register_view.html', {
        'form': form,
    })"""