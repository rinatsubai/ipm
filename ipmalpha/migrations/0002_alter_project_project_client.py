# Generated by Django 4.2.7 on 2023-11-28 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipmclients', '0001_initial'),
        ('ipmalpha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ipmclients.client'),
        ),
    ]
