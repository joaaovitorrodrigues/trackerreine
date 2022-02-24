from django.urls import path

from . import views

app_name = 'escritorio'

urlpatterns = [

    path('escritorio/', views.escritorios, name='escritorio'),
    path('escritorio/adicionar/',
         views.escritorio_add, name='escritorio_add'),
    path('escritorio/editar/<int:id>',
         views.escritorio_edit, name='escritorio_edit'),
]
