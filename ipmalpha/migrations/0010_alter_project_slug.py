# Generated by Django 4.2.7 on 2023-12-07 22:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ipmalpha', '0009_alter_project_project_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
