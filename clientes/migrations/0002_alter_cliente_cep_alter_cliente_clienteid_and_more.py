# Generated by Django 4.0.1 on 2022-02-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.IntegerField(max_length=20, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='clienteid',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Cliente ID'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(max_length=15, unique=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=12, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='datanascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ie',
            field=models.CharField(max_length=15, verbose_name='IE'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='inadimplencia',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='', max_length=2, verbose_name='Inadimplência'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nomecliente',
            field=models.CharField(max_length=50, verbose_name='Nome Cliente/Razão Social'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(max_length=12, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='statuscliente',
            field=models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], default='', max_length=2, verbose_name='Status'),
        ),
    ]
