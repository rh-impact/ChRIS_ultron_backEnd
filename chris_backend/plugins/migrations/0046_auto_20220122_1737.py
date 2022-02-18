# Generated by Django 2.2.24 on 2022-01-22 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0045_computeresource_max_job_exec_seconds'),
    ]

    operations = [
        migrations.AddField(
            model_name='computeresource',
            name='compute_auth_token',
            field=models.CharField(blank=True, default='initial_token', max_length=500),
        ),
        migrations.AddField(
            model_name='computeresource',
            name='compute_auth_url',
            field=models.URLField(blank=True, max_length=350),
        ),
        migrations.AddField(
            model_name='computeresource',
            name='compute_password',
            field=models.CharField(max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computeresource',
            name='compute_user',
            field=models.CharField(max_length=32),
            preserve_default=False,
        ),
    ]