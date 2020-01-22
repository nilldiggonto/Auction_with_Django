# Generated by Django 2.2.2 on 2019-09-23 00:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0002_auto_20190922_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_price',
            name='bid_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 28, 6, 37, 49, 691862), null=True),
        ),
    ]