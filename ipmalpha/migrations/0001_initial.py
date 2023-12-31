# Generated by Django 4.2.7 on 2023-11-28 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=100)),
                ('status_color', models.CharField(default='000000', max_length=6)),
            ],
            options={
                'verbose_name': 'status',
                'verbose_name_plural': 'statuses',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=512)),
                ('project_created', models.DateField(null=True)),
                ('project_finished', models.DateField(null=True)),
                ('project_client', models.CharField(max_length=512)),
                ('project_product', models.CharField(max_length=512)),
                ('project_sum', models.IntegerField(default=0)),
                ('project_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ipmalpha.status')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'ordering': ['id'],
            },
        ),
    ]
