# Generated by Django 2.2.2 on 2019-10-04 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0017_auto_20191004_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 9, 21, 49, 43, 130361), null=True),
        ),
    ]