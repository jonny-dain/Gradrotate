# Generated by Django 4.1.2 on 2022-11-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_job_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='manager_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
