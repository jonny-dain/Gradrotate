# Generated by Django 4.1.2 on 2022-12-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_joblocation_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='daily_tasks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
