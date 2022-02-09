
from django.contrib import admin

from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['clienteid', 'statuscliente',
                    'nomecliente', 'cpf', 'email', 'data_cadastro']

    list_display_links = ['nomecliente', ]


admin.site.register(Cliente, ClienteAdmin)
