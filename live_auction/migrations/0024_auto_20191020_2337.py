# Generated by Django 2.2.2 on 2019-10-20 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_auction', '0023_auto_20191020_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live_second_timer',
            name='end_timer',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 20, 23, 42, 50, 153643), null=True),
        ),
        migrations.AlterField(
            model_name='productlive',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 21, 23, 37, 50, 152642), null=True),
        ),
    ]
