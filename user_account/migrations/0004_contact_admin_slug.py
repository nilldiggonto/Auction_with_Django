# Generated by Django 2.2.2 on 2019-10-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0003_contact_admin_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_admin',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
