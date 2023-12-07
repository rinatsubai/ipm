# Generated by Django 4.2.7 on 2023-12-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipmclients', '0004_client_slug'),
        ('ipmalpha', '0006_remove_project_project_client_project_project_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_client',
        ),
        migrations.AddField(
            model_name='project',
            name='project_client',
            field=models.ManyToManyField(null=True, to='ipmclients.client'),
        ),
    ]