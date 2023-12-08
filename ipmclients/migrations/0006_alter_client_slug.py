# Generated by Django 4.2.7 on 2023-12-07 22:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ipmclients', '0005_alter_client_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
