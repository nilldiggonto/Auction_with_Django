# Generated by Django 2.2.2 on 2019-10-09 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0033_auto_20191008_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 15, 0, 10, 10, 577583), null=True),
        ),
    ]
