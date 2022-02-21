
from django.contrib import admin

from .models import Veiculo


class VeiculoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Veiculo, VeiculoAdmin)
