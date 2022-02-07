from unittest import TestCase

from django.test import TestCase as DjangoTestCase
from django.urls import reverse
from parameterized import parameterized
from users.forms import RegisterForm


class UserRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Digite seu usuário'),
        ('email', 'Digite seu e-mail'),
        ('first_name', 'Digite seu nome'),
        ('last_name', 'Digite seu sobrenome'),
        ('password', 'Digite sua senha'),
        ('confirmacao', 'Repita sua senha'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        ('username', 'Usuário'),
        ('first_name', 'Nome'),
        ('last_name', 'Sobrenome'),
        ('email', 'E-mail'),
        ('password', 'Senha'),
        ('confirmacao', 'Confirmação de senha'),
    ])
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)


class UsersRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@any.com',
            'password': 'StrongPassword1@',
            'confirmacao': 'StrongPassword1@',
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('username', 'Esse campo não pode estar vazio'),
        ('first_name', 'Esse campo não pode estar vazio'),
        ('last_name', 'Esse campo não pode estar vazio'),
        ('password', 'Senha não pode estar vazia'),
        ('confirmacao', 'Confirmação de senha não pode estar vazia'),
        ('email', 'Digite corretamente seu e-mail'),
    ])
    def testes_campos_vazios(self, field, msg):
        self.form_data[field] = ''
        url = reverse('users:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))

    # FUNÇÃO PARA TESTAR CAMPO SENHA E CONFIRMACAO
    def test_campos_senhas_e_confirmacao_iguais(self):
        self.form_data['password'] = 'abc123zKb'
        self.form_data['confirmacao'] = 'abc1234po'

        url = reverse('users:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Senha e confirmação de senha não são iguais'

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

        self.form_data['password'] = 'abc1234po'
        self.form_data['confirmacao'] = 'abc1234po'

        url = reverse('users:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertNotIn(msg, response.content.decode('utf-8'))
