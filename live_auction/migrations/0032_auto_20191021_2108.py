# Generated by Django 2.2.2 on 2019-10-21 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_auction', '0031_auto_20191020_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live_second_timer',
            name='end_timer',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 21, 21, 13, 43, 172692), null=True),
        ),
        migrations.AlterField(
            model_name='productlive',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 22, 21, 8, 43, 171191), null=True),
        ),
    ]
