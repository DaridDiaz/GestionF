# Generated by Django 3.2.5 on 2021-07-11 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_Clientes', '0005_cuentas'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuentas',
            name='nombre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_Clientes.clientes'),
        ),
    ]