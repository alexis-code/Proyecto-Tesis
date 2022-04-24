# Generated by Django 3.2.4 on 2021-11-20 17:30

from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='det_diagnosticodetalle',
            fields=[
                ('id_det_detalle_diagnostico', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'detallediagnostico',
                'verbose_name_plural': 'detallediagnosticos',
                'db_table': 'det_diagnosticodetalle',
            },
        ),
        migrations.CreateModel(
            name='Epicrisis',
            fields=[
                ('id_epicrisisPK', models.AutoField(primary_key=True, serialize=False)),
                ('medico_updated', models.CharField(blank=True, default='-', max_length=50, null=True, verbose_name='Último en Modificar')),
                ('total_dias', models.IntegerField(default=0, verbose_name='Total Días en Hospital')),
                ('proc_mayores', models.TextField(verbose_name='Procedimientos Mayores')),
                ('resumen_evolucion', models.TextField(verbose_name='Resumen de la evolución hospitalaria')),
                ('complicaciones', models.TextField(verbose_name='Complicaciones')),
                ('intervenciones', models.TextField(default='-', verbose_name='Intervenciones Quirurgicas')),
                ('estudios', models.TextField(default='-', verbose_name='Estudios Diagnósticos realizados')),
                ('estudio_imagenes', models.TextField(default='-', verbose_name='Estudio de Imagenes')),
                ('condicion_alta', models.CharField(max_length=50, verbose_name='Condición al alta')),
                ('contra_referido', models.CharField(max_length=5, verbose_name='Contra Referido')),
                ('motivo_alta', models.CharField(max_length=200, verbose_name='Motivo de alta')),
                ('motivo_descripcion', models.TextField(blank=True, null=True, verbose_name='Motivo')),
                ('plan', models.TextField(default='-', verbose_name='Plan de Tratamiento al alta')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('referido_centro', models.CharField(blank=True, default='-', max_length=150, null=True)),
                ('red', models.CharField(blank=True, default='-', max_length=50, null=True)),
                ('estado', models.CharField(blank=True, default='Activo', max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'epicrisi',
                'verbose_name_plural': 'epicrisis',
                'db_table': 'tb_epicrisis',
                'ordering': ['-id_epicrisisPK'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalEpicrisis',
            fields=[
                ('id_epicrisisPK', models.IntegerField(blank=True, db_index=True)),
                ('medico_updated', models.CharField(blank=True, default='-', max_length=50, null=True, verbose_name='Último en Modificar')),
                ('total_dias', models.IntegerField(default=0, verbose_name='Total Días en Hospital')),
                ('proc_mayores', models.TextField(verbose_name='Procedimientos Mayores')),
                ('resumen_evolucion', models.TextField(verbose_name='Resumen de la evolución hospitalaria')),
                ('complicaciones', models.TextField(verbose_name='Complicaciones')),
                ('intervenciones', models.TextField(default='-', verbose_name='Intervenciones Quirurgicas')),
                ('estudios', models.TextField(default='-', verbose_name='Estudios Diagnósticos realizados')),
                ('estudio_imagenes', models.TextField(default='-', verbose_name='Estudio de Imagenes')),
                ('condicion_alta', models.CharField(max_length=50, verbose_name='Condición al alta')),
                ('contra_referido', models.CharField(max_length=5, verbose_name='Contra Referido')),
                ('motivo_alta', models.CharField(max_length=200, verbose_name='Motivo de alta')),
                ('motivo_descripcion', models.TextField(blank=True, null=True, verbose_name='Motivo')),
                ('plan', models.TextField(default='-', verbose_name='Plan de Tratamiento al alta')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('referido_centro', models.CharField(blank=True, default='-', max_length=150, null=True)),
                ('red', models.CharField(blank=True, default='-', max_length=50, null=True)),
                ('estado', models.CharField(blank=True, default='Activo', max_length=20, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical epicrisi',
                'db_table': 'audit_epicrisis',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
