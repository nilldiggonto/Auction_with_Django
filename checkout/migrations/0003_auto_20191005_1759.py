# Generated by Django 2.2.2 on 2019-10-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20191005_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkousystem',
            name='p_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
