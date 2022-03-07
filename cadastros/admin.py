from django.contrib import admin

from .models import Filial, Grupoveiculo, Motorista


class FilialAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_filial',
                    'email', ]

    list_display_links = ['nome_filial', ]
    search_fields = 'nome_filial', 'email'
    list_per_page = 15
    ordering = 'id',


class GrupoveiculoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_grupo',
                    'email', ]

    list_display_links = ['nome_grupo', ]
    search_fields = 'nome_grupo', 'email'
    list_per_page = 15
    ordering = 'id',


class MotoristaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_motorista',
                    'cpf_motorista', 'email', 'filial', ]

    list_display_links = ['nome_motorista', ]
    search_fields = 'nome_motorista', 'email', 'filial'
    list_per_page = 15
    ordering = 'id',


# Registra os models /admin/
admin.site.register(Motorista, MotoristaAdmin)
admin.site.register(Filial, FilialAdmin)
admin.site.register(Grupoveiculo, GrupoveiculoAdmin)
