# Generated by Django 5.1 on 2024-10-03 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0024_remove_ordenproduccion_noordenproduccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenproduccion',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='ordenproduccion',
            name='material',
        ),
        migrations.RemoveField(
            model_name='ordenproduccion',
            name='nolote',
        ),
        migrations.RemoveField(
            model_name='ordenproduccion',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='ordenproduccion',
            name='skump',
        ),
        migrations.RemoveField(
            model_name='ordenproduccion',
            name='surtio',
        ),
        migrations.RemoveField(
            model_name='ordenproduccion',
            name='unidad',
        ),
        migrations.RemoveField(
            model_name='ordenproduccion',
            name='verifico',
        ),
        migrations.AddField(
            model_name='ordenproduccion',
            name='noordenproduccion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='No. Orden Produccion'),
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skump', models.CharField(blank=True, max_length=100, null=True, verbose_name='SKU MP')),
                ('material', models.CharField(blank=True, max_length=100, null=True, verbose_name='Material')),
                ('nolote', models.CharField(blank=True, max_length=100, null=True, verbose_name='No. Lpte')),
                ('unidad', models.CharField(blank=True, max_length=100, null=True, verbose_name='Unidad')),
                ('cantidad', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cantidad')),
                ('surtio', models.CharField(blank=True, max_length=100, null=True, verbose_name='Surtió')),
                ('verifico', models.CharField(blank=True, max_length=100, null=True, verbose_name='Verificó')),
                ('observaciones', models.CharField(blank=True, max_length=100, null=True, verbose_name='Observaciones')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='contacts.ordenproduccion')),
            ],
        ),
    ]
