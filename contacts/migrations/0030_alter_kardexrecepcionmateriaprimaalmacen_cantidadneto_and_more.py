# Generated by Django 5.1 on 2024-11-21 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0029_alter_kardexrecepcionmateriaprimaalmacen_cantidadneto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='cantidadneto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kardex_cantidadneto', to='contacts.formatorecepcionmateriaprima'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='codigoproveedorcliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kardex_codigoproveedorcliente', to='contacts.formatorecepcionmateriaprima'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='fechacaducidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kardex_fechacaducidad', to='contacts.formatorecepcionmateriaprima'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='fechaentrada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kardex_fechaentrada', to='contacts.formatorecepcionmateriaprima'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='materiaprima',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kardex_materiaprima', to='contacts.formatorecepcionmateriaprima'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='noloteseprisa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kardex_noloteseprisa', to='contacts.formatorecepcionmateriaprima'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='sku',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kardex_sku', to='contacts.formatorecepcionmateriaprima'),
        ),
    ]
