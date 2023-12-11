# Generated by Django 4.2.7 on 2023-12-11 21:44

import autoslug.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ipmclients', '0008_alter_client_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='newslug',
            field=autoslug.fields.AutoSlugField(default=django.utils.timezone.now, editable=False, populate_from='id'),
            preserve_default=False,
        ),
    ]