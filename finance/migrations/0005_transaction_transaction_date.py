# Generated by Django 4.2.7 on 2023-12-12 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_alter_transaction_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
