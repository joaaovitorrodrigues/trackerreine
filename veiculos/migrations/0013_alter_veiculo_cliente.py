# Generated by Django 4.0.1 on 2022-03-07 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0016_remove_cliente_username'),
        ('veiculos', '0012_alter_veiculo_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='cliente',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, to='clientes.cliente'),
            preserve_default=False,
        ),
    ]
