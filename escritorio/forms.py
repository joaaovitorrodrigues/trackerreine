from django import forms

from .models import Escritorio


class EscritorioForm(forms.ModelForm):
    class Meta:
        model = Escritorio
        exclude = ()

        widgets = {
            'nome_escritorio': forms.TextInput(attrs={'class': 'form-control',
                                                      'autofocus': ''}),
            'descricao_escritorio': forms.TextInput(attrs={'class':
                                                           'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
