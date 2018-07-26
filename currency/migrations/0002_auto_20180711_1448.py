# Generated by Django 2.0.6 on 2018-07-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='sync_deposit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pair',
            name='note',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='pair',
            name='req_note',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='pair',
            name='tag',
            field=models.CharField(default='', max_length=200),
        ),
    ]
