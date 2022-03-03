from django.urls import path

from . import views

app_name = 'cadastros'

urlpatterns = [

    path('', views.cadastro, name='cadastros'),
    path('filial/', views.filial, name='filial'),
    path('motorista/', views.motorista, name='motorista'),
    path('cerca/', views.cerca, name='cerca'),
]
