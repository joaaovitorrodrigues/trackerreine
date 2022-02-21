from django import forms

from .models import Grupoveiculo


class GrupoveiculoForm(forms.ModelForm):
    class Meta:
        model = Grupoveiculo
        exclude = ()

        widgets = {
            'nome_grupo': forms.TextInput(attrs={'class': 'form-control',
                                                 'autofocus': ''}),
            'descricao_grupo': forms.TextInput(attrs={'class': 'form-control'
                                                      }),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
