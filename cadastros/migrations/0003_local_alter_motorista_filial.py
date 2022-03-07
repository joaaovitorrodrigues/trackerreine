# Generated by Django 4.0.1 on 2022-03-07 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_remove_filial_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cerca', models.CharField(max_length=100)),
                ('descricao_cerca', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='motorista',
            name='filial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.filial'),
        ),
    ]