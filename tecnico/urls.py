from django.urls import path

from . import views

urlpatterns = [
    path('', views.tecnicos, name="tecnicos"),
]
