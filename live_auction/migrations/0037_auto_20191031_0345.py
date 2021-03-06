# Generated by Django 2.2.2 on 2019-10-30 21:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
import live_auction.models


class Migration(migrations.Migration):

    dependencies = [
        ('live_auction', '0036_auto_20191021_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live_second_timer',
            name='end_timer',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 31, 3, 50, 20, 912205), null=True),
        ),
        migrations.AlterField(
            model_name='productlive',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 1, 3, 45, 20, 910704), null=True),
        ),
        migrations.AlterField(
            model_name='productlive',
            name='image',
            field=models.ImageField(upload_to=live_auction.models.upload_image_path, verbose_name='Image_1'),
        ),
        migrations.AlterField(
            model_name='productlive',
            name='p_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.Category_post', verbose_name='Category'),
        ),
    ]
