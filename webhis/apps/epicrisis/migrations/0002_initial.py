# Generated by Django 3.2.4 on 2021-11-20 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('evolucion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('epicrisis', '0001_initial'),
        ('codigocie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalepicrisis',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalepicrisis',
            name='id_evolucionFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evolucion.evolucion'),
        ),
        migrations.AddField(
            model_name='historicalepicrisis',
            name='id_medicoFK',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='epicrisis',
            name='id_evolucionFK',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evolucion.evolucion'),
        ),
        migrations.AddField(
            model_name='epicrisis',
            name='id_medicoFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='det_diagnosticodetalle',
            name='id_codigocieFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codigocie.codigocie'),
        ),
        migrations.AddField(
            model_name='det_diagnosticodetalle',
            name='id_epicrisisFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epicrisis.epicrisis'),
        ),
    ]