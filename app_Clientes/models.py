from app_Clientes.views import clientes
from django.db import models
from django.db.models.fields import DateTimeField

class Clientes(models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    direccion = models.CharField(max_length=40)
    fecha = models.DateField()
    telefono = models.CharField(max_length=35)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Cuentas(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField()
    saldo = models.DecimalField(max_digits=50, decimal_places=3)
    clientes = models.ForeignKey(Clientes,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.saldo

class Transacciones(models.Model):
    deposito = models.DecimalField(max_digits=50, decimal_places=3)
    retiro = models.DecimalField(max_digits=50, decimal_places=3)
    tranferencia = models.DecimalField(max_digits=50, decimal_places=3)

    


    
