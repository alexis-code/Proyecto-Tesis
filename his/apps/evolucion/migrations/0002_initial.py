# Generated by Django 3.2.4 on 2021-11-20 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('historiaclinica', '0001_initial'),
        ('medicamento', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evolucion', '0001_initial'),
        ('resultadolaboratorio', '0001_initial'),
        ('cultivo', '0001_initial'),
        ('examenfisico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalevolucion',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalevolucion',
            name='id_examenfisicoFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='examenfisico.examenfisico'),
        ),
        migrations.AddField(
            model_name='historicalevolucion',
            name='id_historiaclinicaFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='historiaclinica.historiaclinica'),
        ),
        migrations.AddField(
            model_name='historicalevolucion',
            name='id_medicoFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalevolucion',
            name='id_resultadolabFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='resultadolaboratorio.resultadolab'),
        ),
        migrations.AddField(
            model_name='historicaldet_tratmiento_evolucion',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldet_tratmiento_evolucion',
            name='id_evolucionFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evolucion.evolucion'),
        ),
        migrations.AddField(
            model_name='historicaldet_tratmiento_evolucion',
            name='id_medicamentoFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='medicamento.medicamento'),
        ),
        migrations.AddField(
            model_name='historicaldet_cultivo_evolucion',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldet_cultivo_evolucion',
            name='id_cultivoFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cultivo.cultivo'),
        ),
        migrations.AddField(
            model_name='historicaldet_cultivo_evolucion',
            name='id_evolucionFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evolucion.evolucion'),
        ),
        migrations.AddField(
            model_name='evolucion',
            name='id_examenfisicoFK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='examenfisico.examenfisico'),
        ),
        migrations.AddField(
            model_name='evolucion',
            name='id_historiaclinicaFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='historiaclinica.historiaclinica'),
        ),
        migrations.AddField(
            model_name='evolucion',
            name='id_medicoFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evolucion',
            name='id_resultadolabFK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='resultadolaboratorio.resultadolab'),
        ),
        migrations.AddField(
            model_name='det_tratmiento_evolucion',
            name='id_evolucionFK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evolucion.evolucion'),
        ),
        migrations.AddField(
            model_name='det_tratmiento_evolucion',
            name='id_medicamentoFK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medicamento.medicamento'),
        ),
        migrations.AddField(
            model_name='det_cultivo_evolucion',
            name='id_cultivoFK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cultivo.cultivo'),
        ),
        migrations.AddField(
            model_name='det_cultivo_evolucion',
            name='id_evolucionFK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evolucion.evolucion'),
        ),
    ]
