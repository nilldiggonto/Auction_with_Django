# Generated by Django 2.2.2 on 2019-10-05 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0020_auto_20191005_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 10, 14, 53, 13, 709055), null=True),
        ),
    ]
