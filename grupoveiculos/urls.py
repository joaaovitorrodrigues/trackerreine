from django.urls import path

from . import views

app_name = 'grupoveiculo'

urlpatterns = [

    path('grupoveiculos/', views.grupoveiculo, name='grupoveiculos'),
    path('grupoveiculos/adicionar/',
         views.grupoveiculos_add, name='grupoveiculos_add'),
    path('grupoveiculos/editar/<int:id>', views.grupoveiculo_edit,
         name='grupoveiculos_edit'),
]
