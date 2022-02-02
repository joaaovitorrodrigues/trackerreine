from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'password': 'Senha',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite seu usuário',
            }),

            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu nome',
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu sobrenome',
            }),

            'email': forms.TextInput(attrs={
                'placeholder': 'Digite seu e-mail',
            }),

            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha',
            }),
        }

