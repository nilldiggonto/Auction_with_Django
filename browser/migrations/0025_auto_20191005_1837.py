# Generated by Django 2.2.2 on 2019-10-05 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0024_auto_20191005_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 10, 18, 37, 58, 363072), null=True),
        ),
    ]
