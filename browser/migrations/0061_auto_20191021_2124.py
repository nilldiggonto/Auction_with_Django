# Generated by Django 2.2.2 on 2019-10-21 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0060_auto_20191021_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 26, 21, 24, 43, 330582), null=True),
        ),
    ]