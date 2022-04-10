# Generated by Django 3.2.4 on 2021-11-20 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('indicacion', '0001_initial'),
        ('medicamento', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evolucion', '0002_initial'),
        ('medidasgenerales', '0001_initial'),
        ('solicitudlaboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicacion',
            name='id_medicoFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalindicacion',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalindicacion',
            name='id_evolucionFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evolucion.evolucion'),
        ),
        migrations.AddField(
            model_name='historicalindicacion',
            name='id_medicoFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldet_tratamiento_indicacion',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldet_tratamiento_indicacion',
            name='id_indicacionFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicacion.indicacion'),
        ),
        migrations.AddField(
            model_name='historicaldet_tratamiento_indicacion',
            name='id_medicamentoFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='medicamento.medicamento'),
        ),
        migrations.AddField(
            model_name='historicaldet_solucion',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldet_solucion',
            name='id_indicacionFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicacion.indicacion'),
        ),
        migrations.AddField(
            model_name='historicaldet_solucion',
            name='id_medicamentoFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='medicamento.medicamento'),
        ),
        migrations.AddField(
            model_name='historicaldet_solicitud_indicacion',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldet_solicitud_indicacion',
            name='id_indicacionFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicacion.indicacion'),
        ),
        migrations.AddField(
            model_name='historicaldet_solicitud_indicacion',
            name='id_solicitud_laboratioFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='solicitudlaboratorio.solicitudlaboratorio'),
        ),
        migrations.AddField(
            model_name='historicaldet_indicacion_medida_general',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldet_indicacion_medida_general',
            name='id_indicacionFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indicacion.indicacion'),
        ),
        migrations.AddField(
            model_name='historicaldet_indicacion_medida_general',
            name='id_medida_generalFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='medidasgenerales.medidasgenerales'),
        ),
        migrations.AddField(
            model_name='det_tratamiento_indicacion',
            name='id_indicacionFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicacion.indicacion'),
        ),
        migrations.AddField(
            model_name='det_tratamiento_indicacion',
            name='id_medicamentoFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicamento.medicamento'),
        ),
        migrations.AddField(
            model_name='det_solucion',
            name='id_indicacionFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicacion.indicacion'),
        ),
        migrations.AddField(
            model_name='det_solucion',
            name='id_medicamentoFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicamento.medicamento'),
        ),
        migrations.AddField(
            model_name='det_solicitud_indicacion',
            name='id_indicacionFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicacion.indicacion'),
        ),
        migrations.AddField(
            model_name='det_solicitud_indicacion',
            name='id_solicitud_laboratioFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudlaboratorio.solicitudlaboratorio'),
        ),
        migrations.AddField(
            model_name='det_indicacion_medida_general',
            name='id_indicacionFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicacion.indicacion'),
        ),
        migrations.AddField(
            model_name='det_indicacion_medida_general',
            name='id_medida_generalFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medidasgenerales.medidasgenerales'),
        ),
    ]