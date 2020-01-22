# Generated by Django 2.2.2 on 2019-09-30 14:00

import browser.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0008_auto_20190927_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=browser.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 5, 20, 0, 56, 529580), null=True),
        ),
    ]