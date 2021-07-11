# Generated by Django 3.2.5 on 2021-07-11 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Clientes', '0002_alter_clientes_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposito', models.DecimalField(decimal_places=3, max_digits=50)),
                ('retiro', models.DecimalField(decimal_places=3, max_digits=50)),
                ('tranferencia', models.DecimalField(decimal_places=2, max_digits=50)),
            ],
        ),
    ]
