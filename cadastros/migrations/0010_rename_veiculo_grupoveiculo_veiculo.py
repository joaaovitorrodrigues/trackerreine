# Generated by Django 4.0.1 on 2022-03-07 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_grupoveiculo_veiculo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grupoveiculo',
            old_name='Veiculo',
            new_name='veiculo',
        ),
    ]