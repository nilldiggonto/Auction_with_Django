# Generated by Django 2.2.2 on 2019-10-20 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0047_auto_20191019_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 25, 15, 57, 54, 965948), null=True),
        ),
    ]
