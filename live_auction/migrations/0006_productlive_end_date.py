# Generated by Django 2.2.2 on 2019-10-07 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_auction', '0005_auto_20191007_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlive',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 8, 22, 33, 13, 697076), null=True),
        ),
    ]
