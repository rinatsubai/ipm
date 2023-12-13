# Generated by Django 4.2.7 on 2023-12-12 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipmalpha', '0017_alter_project_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=512)),
                ('amount', models.PositiveIntegerField()),
                ('flow', models.CharField(choices=[('IN', 'Income'), ('OU', 'Outcome'), ('SA', 'Salary')], default='IN', max_length=2)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ipmalpha.project', verbose_name='Project')),
            ],
        ),
    ]
