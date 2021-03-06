# Generated by Django 2.2.2 on 2019-10-01 20:04

from django.conf import settings
from django.db import migrations, models
import live_auction.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('browser', '0013_auto_20191002_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to=live_auction.models.upload_image_path, verbose_name='Image')),
                ('live', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('p_category', models.ForeignKey(blank=True, null=True, on_delete='DO_NOTHING', to='browser.Category_post', verbose_name='Category')),
                ('user', models.ForeignKey(on_delete='DO_NOTHING', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
