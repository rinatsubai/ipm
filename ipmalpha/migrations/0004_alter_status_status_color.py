# Generated by Django 4.2.7 on 2023-12-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipmalpha', '0003_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status_color',
            field=models.CharField(default='table-primary', max_length=512),
        ),
    ]
