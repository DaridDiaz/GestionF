# Generated by Django 3.2.5 on 2021-07-11 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_Clientes', '0006_cuentas_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuentas',
            name='nombre',
        ),
    ]
