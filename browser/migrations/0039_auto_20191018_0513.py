# Generated by Django 2.2.2 on 2019-10-17 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0038_auto_20191018_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 23, 5, 13, 14, 609352), null=True),
        ),
    ]
