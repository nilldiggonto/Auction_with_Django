# Generated by Django 2.2.2 on 2019-10-04 15:50

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billing_address', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing_profile',
            name='fullname',
        ),
        migrations.AddField(
            model_name='billing_profile',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='billing_profile',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='billing_profile',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billing_profile',
            name='user',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete='DO_NOTHING', to=settings.AUTH_USER_MODEL),
        ),
    ]
