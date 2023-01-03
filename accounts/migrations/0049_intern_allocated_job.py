# Generated by Django 4.1.2 on 2023-01-03 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0048_admin_total_interns_admin_total_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern',
            name='allocated_job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.job'),
        ),
    ]
