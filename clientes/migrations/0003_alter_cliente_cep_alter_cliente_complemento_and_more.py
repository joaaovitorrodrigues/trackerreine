# Generated by Django 4.0.1 on 2022-02-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_cep_alter_cliente_clienteid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=20, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='complemento',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, verbose_name='CPF'),
        ),
    ]
