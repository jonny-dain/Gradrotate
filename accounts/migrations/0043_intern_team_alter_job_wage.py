# Generated by Django 4.1.2 on 2022-12-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_alter_job_daily_tasks_alter_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern',
            name='team',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='wage',
            field=models.IntegerField(default=15000),
        ),
    ]
