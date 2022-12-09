# Generated by Django 4.1.2 on 2022-12-08 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_remove_intern_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
        migrations.AddField(
            model_name='job',
            name='job_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.joblocation'),
        ),
    ]
