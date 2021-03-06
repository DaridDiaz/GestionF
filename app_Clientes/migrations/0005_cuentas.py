# Generated by Django 3.2.5 on 2021-07-11 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Clientes', '0004_alter_transacciones_tranferencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField()),
                ('saldo', models.DecimalField(decimal_places=3, max_digits=50)),
            ],
        ),
    ]
