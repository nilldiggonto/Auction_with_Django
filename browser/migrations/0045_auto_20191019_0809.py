# Generated by Django 2.2.2 on 2019-10-19 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0044_auto_20191018_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 24, 8, 9, 47, 310370), null=True),
        ),
    ]
