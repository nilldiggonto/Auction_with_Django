# Generated by Django 2.2.2 on 2019-10-01 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0011_auto_20190930_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 7, 1, 32, 10, 878703), null=True),
        ),
    ]
