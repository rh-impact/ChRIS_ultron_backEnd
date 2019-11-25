# Generated by Django 2.1.4 on 2019-02-21 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipelineinstances', '0001_initial'),
        ('plugininstances', '0005_auto_20190221_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='plugininstance',
            name='pipeline_inst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plugin_instances', to='pipelineinstances.PipelineInstance'),
        ),
    ]