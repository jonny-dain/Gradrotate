# Generated by Django 4.1.2 on 2023-01-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_job_allocated_intern'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='notify_allocations',
            field=models.BooleanField(default=False),
        ),
    ]
