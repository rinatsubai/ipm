# Generated by Django 4.2.7 on 2023-12-15 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipmalpha', '0017_alter_project_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=512, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.ForeignKey(default='Draft', null=True, on_delete=django.db.models.deletion.PROTECT, to='ipmalpha.status'),
        ),
    ]
