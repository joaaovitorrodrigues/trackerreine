# Generated by Django 4.0.1 on 2022-03-07 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_filial_data_cadastro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filial',
            options={'ordering': ('nome_filial',), 'verbose_name_plural': 'Filiais'},
        ),
    ]
