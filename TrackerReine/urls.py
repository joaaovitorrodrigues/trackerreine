from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('monitoramento.urls')),
    path('users/', include('users.urls')),
    path('clientes/', include('clientes.urls')),
    path('veiculos/', include('veiculos.urls')),
    path('', include('grupoveiculos.urls')),
    path('', include('escritorio.urls')),
    path('', include('tecnico.urls')),
    path('cadastro/', include('cadastros.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
