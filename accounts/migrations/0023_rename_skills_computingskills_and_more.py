# Generated by Django 4.1.2 on 2022-11-25 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_remove_skills_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='ComputingSkills',
        ),
        migrations.RenameField(
            model_name='intern',
            old_name='skills',
            new_name='computing_skills',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='skills',
            new_name='computing_skills',
        ),
    ]
