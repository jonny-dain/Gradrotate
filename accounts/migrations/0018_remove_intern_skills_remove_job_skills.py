# Generated by Django 4.1.2 on 2022-11-22 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_intern_location_intern_remote_alter_admin_phase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intern',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='job',
            name='skills',
        ),
    ]
