# Generated by Django 3.2.5 on 2021-07-11 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_Clientes', '0008_cuentas_clientes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transacciones',
        ),
    ]