from django.urls import path

from . import views

app_name = 'monitoramento'
urlpatterns = [
    path('monitoramento/', views.monitoramento, name='monitoramento'),
]
