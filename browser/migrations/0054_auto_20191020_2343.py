# Generated by Django 2.2.2 on 2019-10-20 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0053_auto_20191020_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 25, 23, 43, 51, 288684), null=True),
        ),
    ]
