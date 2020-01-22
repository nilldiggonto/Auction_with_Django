# Generated by Django 2.2.2 on 2019-10-09 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_auction', '0008_auto_20191008_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live_second_timer',
            name='end_timer',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 10, 0, 15, 10, 581586), null=True),
        ),
        migrations.AlterField(
            model_name='product_price_live',
            name='current_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='productlive',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 11, 0, 10, 10, 580585), null=True),
        ),
    ]
