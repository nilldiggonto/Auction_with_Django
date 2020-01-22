# Generated by Django 2.2.2 on 2019-09-30 14:38

import browser.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0009_auto_20190930_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 5, 20, 38, 15, 640657), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=browser.models.upload_image_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=33.33, max_digits=10, verbose_name='Market Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stating_price',
            field=models.DecimalField(decimal_places=2, default=33.33, max_digits=10, verbose_name='Starter Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Title'),
        ),
    ]