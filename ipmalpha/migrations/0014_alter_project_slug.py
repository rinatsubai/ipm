# Generated by Django 4.2.7 on 2023-12-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipmalpha', '0013_alter_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
