# Generated by Django 4.1.2 on 2022-11-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_intern_skills_job_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='category',
            field=models.CharField(choices=[('Coding', 'Coding'), ('Project Management', 'Project Management')], max_length=200, null=True),
        ),
    ]
