# Generated by Django 2.2.2 on 2019-10-02 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0013_auto_20191002_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 7, 19, 42, 10, 611053), null=True),
        ),
    ]
