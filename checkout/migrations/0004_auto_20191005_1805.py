# Generated by Django 2.2.2 on 2019-10-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20191005_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkousystem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
