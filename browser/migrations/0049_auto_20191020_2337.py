# Generated by Django 2.2.2 on 2019-10-20 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0048_auto_20191020_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 25, 23, 37, 50, 148639), null=True),
        ),
    ]