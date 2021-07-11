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
        return f'{self.nombre} {self.apellido}'

class Cuentas(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField()
    saldo = models.DecimalField(max_digits=50, decimal_places=3)
    clientes = models.ForeignKey(Clientes,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Cuentas: {self.saldo} - cliente: {self.clientes}'


class deposito(models.Model):
    deposito = models.DecimalField(max_digits=50, decimal_places=3)
    clientes = models.ForeignKey(Clientes,on_delete=models.CASCADE, null=True)
    fecha_realizacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'deposito: {self.deposito} - cliente: {self.clientes}'

class retiro(models.Model):
    retiro = models.DecimalField(max_digits=50, decimal_places=3)
    clientes = models.ForeignKey(Clientes,on_delete=models.CASCADE, null=True)
    fecha_realizacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'retiro: {self.deposito} - cliente: {self.clientes}'