# Generated by Django 3.0.4 on 2020-04-01 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0010_auto_20200330_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParametrosSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hospital_parametro', to='pedidos.Tercero', verbose_name='Hospital')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Médico_parametro', to='pedidos.Tercero', verbose_name='Médico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Paciente_parametro', to='pedidos.Tercero', verbose_name='Paciente')),
                ('pagador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pagador_parametro', to='pedidos.Tercero', verbose_name='Pagador')),
                ('solicitud', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Solcicitud_parametro', to='pedidos.Solicitud')),
            ],
            options={
                'verbose_name': 'Parametro Solicitud',
                'verbose_name_plural': 'Parametros Solicitudes',
                'ordering': ['solicitud'],
            },
        ),
    ]