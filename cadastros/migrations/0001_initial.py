# Generated by Django 4.0.1 on 2022-03-02 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0014_alter_cliente_mensalidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_filial', models.CharField(max_length=100)),
                ('descricao_grupo', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filiais', to='clientes.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_motorista', models.CharField(max_length=100)),
                ('cpf_motorista', models.CharField(max_length=100)),
                ('rg_motorista', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motoristas', to='cadastros.filial')),
            ],
        ),
    ]
