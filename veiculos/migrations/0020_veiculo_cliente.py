# Generated by Django 4.0.1 on 2022-03-07 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0016_remove_cliente_username'),
        ('veiculos', '0019_remove_veiculo_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
            preserve_default=False,
        ),
    ]