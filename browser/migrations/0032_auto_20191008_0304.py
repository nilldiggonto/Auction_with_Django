# Generated by Django 2.2.2 on 2019-10-07 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0031_auto_20191007_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 13, 3, 4, 40, 636671), null=True),
        ),
    ]
