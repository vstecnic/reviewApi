# Generated by Django 5.1.4 on 2025-01-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='foto1',
            field=models.CharField(default='None', max_length=550),
        ),
        migrations.AddField(
            model_name='entrada',
            name='foto2',
            field=models.CharField(default='None', max_length=550),
        ),
        migrations.AddField(
            model_name='entrada',
            name='foto3',
            field=models.CharField(default='None', max_length=550),
        ),
    ]
