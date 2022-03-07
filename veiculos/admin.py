
from django.contrib import admin

from .models import Cliente, Veiculo


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['veiculoid', 'statusveiculo',
                    'placaveiculo', 'marcaveiculo', 'modelo', 'chassi',
                    'renavam', 'localinstalacao', 'data_cadastro']

    list_display_links = ['placaveiculo', ]
    search_fields = 'placaveiculo', 'marcaveiculo', 'modelo'
    list_per_page = 15
    ordering = 'veiculoid',


admin.site.register(Veiculo, VeiculoAdmin)
