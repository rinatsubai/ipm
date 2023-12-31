# Generated by Django 4.2.7 on 2023-12-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_alter_transaction_flow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='flow',
            field=models.CharField(choices=[('INC', 'Income'), ('OUT', 'Outcome'), ('SAL', 'Salary')], default='INC', max_length=3),
        ),
    ]
