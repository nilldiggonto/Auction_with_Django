# Generated by Django 2.2.2 on 2019-11-03 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_auction', '0037_auto_20191031_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live_second_timer',
            name='end_timer',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 3, 16, 55, 9, 158046), null=True),
        ),
        migrations.AlterField(
            model_name='productlive',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 4, 16, 50, 9, 156545), null=True),
        ),
    ]