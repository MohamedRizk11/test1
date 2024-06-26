# Generated by Django 5.0.4 on 2024-05-08 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masark', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='road',
            name='id',
        ),
        migrations.RemoveField(
            model_name='station',
            name='id',
        ),
        migrations.AlterField(
            model_name='road',
            name='distance',
            field=models.FloatField(verbose_name='Distance'),
        ),
        migrations.AlterField(
            model_name='road',
            name='road_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Road_id'),
        ),
        migrations.AlterField(
            model_name='road',
            name='time',
            field=models.IntegerField(verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Station_id'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='from_station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_station_tickets', to='masark.station'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='to_station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_station_tickets', to='masark.station'),
        ),
    ]
