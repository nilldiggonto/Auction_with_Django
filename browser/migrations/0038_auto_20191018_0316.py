# Generated by Django 2.2.2 on 2019-10-17 21:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0037_auto_20191018_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 23, 3, 16, 18, 306454), null=True),
        ),
    ]