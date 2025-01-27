# Generated by Django 5.1 on 2024-11-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0032_alter_kardexrecepcionmateriaprimaalmacen_cantidadneto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='cantidadneto',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad Neto'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='codigoproveedorcliente',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Codigo Proveedor o Cliente'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='fechacaducidad',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='fechaentrada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='materiaprima',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Materia Prima'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='noloteseprisa',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='No. Lote Seprisa'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='sku',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='SKU'),
        ),
    ]
