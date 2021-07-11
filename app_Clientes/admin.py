from django.contrib import admin

from .models import Clientes
from .models import Cuentas
from .models import deposito
from .models import retiro

admin.site.register(Clientes)
admin.site.register(Cuentas)
admin.site.register(deposito)
admin.site.register(retiro)