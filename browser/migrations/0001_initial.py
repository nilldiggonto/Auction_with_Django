# Generated by Django 2.2.2 on 2019-09-20 17:37

import browser.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_price', models.DecimalField(decimal_places=2, default=33.33, max_digits=10)),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete='DO_NOTHING', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('day', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=33.33, max_digits=10)),
                ('stating_price', models.DecimalField(decimal_places=2, default=33.33, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to=browser.models.upload_image_path)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete='DO_NOTHING', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
