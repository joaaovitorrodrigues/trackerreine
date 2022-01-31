from django.urls import path

from monitoramento.views import monitoramento

urlpatterns = [
    path('', monitoramento),
]