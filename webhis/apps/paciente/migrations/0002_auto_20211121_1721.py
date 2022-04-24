# Generated by Django 3.2.4 on 2021-11-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpaciente',
            name='nro_documento',
            field=models.IntegerField(db_index=True, verbose_name='Nro de Documento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nro_documento',
            field=models.IntegerField(unique=True, verbose_name='Nro de Documento'),
        ),
    ]
