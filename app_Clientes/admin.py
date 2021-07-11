from django.contrib import admin

from .models import Clientes
from .models import Transacciones
from .models import Cuentas

admin.site.register(Clientes)
admin.site.register(Transacciones)
admin.site.register(Cuentas)