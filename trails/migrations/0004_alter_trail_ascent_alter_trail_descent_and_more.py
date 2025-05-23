# Generated by Django 5.2 on 2025-04-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0003_trailimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='ascent',
            field=models.CharField(help_text='e.g. ~800m', max_length=20),
        ),
        migrations.AlterField(
            model_name='trail',
            name='descent',
            field=models.CharField(help_text='e.g. ~800m', max_length=20),
        ),
        migrations.AlterField(
            model_name='trail',
            name='distance',
            field=models.CharField(help_text='e.g. 14.5 km', max_length=20),
        ),
        migrations.AlterField(
            model_name='trail',
            name='duration',
            field=models.CharField(help_text='e.g. 1 hour, 4h 30min', max_length=20),
        ),
    ]
