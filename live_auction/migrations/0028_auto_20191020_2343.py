# Generated by Django 2.2.2 on 2019-10-20 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_auction', '0027_auto_20191020_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live_second_timer',
            name='end_timer',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 20, 23, 48, 6, 820570), null=True),
        ),
        migrations.AlterField(
            model_name='productlive',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 21, 23, 43, 6, 818569), null=True),
        ),
    ]
