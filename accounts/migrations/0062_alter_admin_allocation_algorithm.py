# Generated by Django 4.1.2 on 2023-02-15 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0061_alter_intern_admin_skills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='allocation_algorithm',
            field=models.CharField(choices=[('Gale Shapely', 'Gale Shapely'), ('Hungarian', 'Hungarian'), ('Pareto', 'Pareto'), ('Random Serial Dictatorship', 'Random Serial Dictatorship')], max_length=200, null=True),
        ),
    ]
