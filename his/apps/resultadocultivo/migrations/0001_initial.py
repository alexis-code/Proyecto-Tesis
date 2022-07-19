# Generated by Django 3.2.4 on 2021-11-20 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('evolucion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cultivo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoCultivo',
            fields=[
                ('id_resultCultivoPK', models.AutoField(primary_key=True, serialize=False)),
                ('medico', models.CharField(default='-', max_length=150, verbose_name='Nombre del Médico')),
                ('medico_udpated', models.CharField(default='-', max_length=150, verbose_name='Último en Modificar')),
                ('resultado_probable', models.CharField(max_length=50, verbose_name='Resultados Probables')),
                ('patogeno', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre del Patógeno')),
                ('sensible', models.CharField(blank=True, max_length=500, null=True, verbose_name='Sensible')),
                ('resistente', models.CharField(blank=True, max_length=500, null=True, verbose_name='Resistente')),
                ('parcial_sensible', models.CharField(blank=True, max_length=500, null=True, verbose_name='Parcialmente Sensible')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name='Comentario')),
                ('estado', models.CharField(default='Activo', max_length=10, verbose_name='Estado')),
                ('id_cultivoFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cultivo.cultivo')),
                ('id_evolucionFK', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evolucion.evolucion')),
            ],
            options={
                'verbose_name': 'resultadocultivo',
                'verbose_name_plural': 'resultadocultivos',
                'db_table': 'tb_resultadoCultivo',
            },
        ),
        migrations.CreateModel(
            name='HistoricalResultadoCultivo',
            fields=[
                ('id_resultCultivoPK', models.IntegerField(blank=True, db_index=True)),
                ('medico', models.CharField(default='-', max_length=150, verbose_name='Nombre del Médico')),
                ('medico_udpated', models.CharField(default='-', max_length=150, verbose_name='Último en Modificar')),
                ('resultado_probable', models.CharField(max_length=50, verbose_name='Resultados Probables')),
                ('patogeno', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre del Patógeno')),
                ('sensible', models.CharField(blank=True, max_length=500, null=True, verbose_name='Sensible')),
                ('resistente', models.CharField(blank=True, max_length=500, null=True, verbose_name='Resistente')),
                ('parcial_sensible', models.CharField(blank=True, max_length=500, null=True, verbose_name='Parcialmente Sensible')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name='Comentario')),
                ('estado', models.CharField(default='Activo', max_length=10, verbose_name='Estado')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('id_cultivoFK', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cultivo.cultivo')),
                ('id_evolucionFK', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evolucion.evolucion')),
            ],
            options={
                'verbose_name': 'historical resultadocultivo',
                'db_table': 'audit_result_cultivo',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]