# Generated by Django 2.2.2 on 2019-10-21 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0057_auto_20191021_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 26, 21, 14, 36, 214190), null=True),
        ),
    ]
