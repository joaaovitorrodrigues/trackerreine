from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Digite seu usuário')
        add_placeholder(self.fields['email'], 'Digite seu e-mail')
        add_placeholder(self.fields['first_name'], 'Digite seu nome')
        add_placeholder(self.fields['last_name'], 'Digite seu sobrenome')
        add_placeholder(self.fields['password'], 'Digite sua senha')
        add_placeholder(self.fields['confirmacao'], 'Repita sua senha')

    # Campo senha com placeholder, mensagens de erro e ajuda de texto
    username = forms.CharField(
        error_messages={'required': 'Esse campo não pode estar vazio'},
        label='Usuário',
    )
    # Campo senha com placeholder, mensagens de erro e ajuda de texto
    first_name = forms.CharField(
        label='Nome',
        error_messages={'required': 'Esse campo não pode estar vazio'},
    )
    # Campo senha com placeholder, mensagens de erro e ajuda de texto
    last_name = forms.CharField(
        label='Sobrenome',
        error_messages={'required': 'Esse campo não pode estar vazio'},
    )
    # Campo senha com placeholder, mensagens de erro e ajuda de texto
    email = forms.EmailField(
        label='E-mail',
        error_messages={'required': 'Digite corretamente seu e-mail'},
    )
    # Campo senha com placeholder, mensagens de erro e ajuda de texto
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(),
        error_messages={'required': 'Senha não pode estar vazia'}
    )

    # Campo confirmação de senha com placeholder, mensagens de erro...
    confirmacao = forms.CharField(
        required=True,
        label='Confirmação de senha',
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Confirmação de senha não pode estar vazia'}

    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    # Validação do campo senha

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirmacao = cleaned_data.get('confirmacao')

        if password != confirmacao:
            raise ValidationError({
                'password': 'Senha e confirmação de senha não são iguais',
                'confirmacao': 'Senha e confirmação de senha não são iguais'
            })
