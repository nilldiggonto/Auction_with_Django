# Generated by Django 2.2.2 on 2019-10-21 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_auction', '0034_auto_20191021_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live_second_timer',
            name='end_timer',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 21, 21, 26, 6, 387199), null=True),
        ),
        migrations.AlterField(
            model_name='productlive',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 22, 21, 21, 6, 385698), null=True),
        ),
    ]
