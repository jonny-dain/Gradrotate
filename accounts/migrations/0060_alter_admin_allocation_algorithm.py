# Generated by Django 4.1.2 on 2023-01-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0059_alter_admin_allocation_algorithm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='allocation_algorithm',
            field=models.CharField(choices=[('Gale Shapely', 'Gale Shapely'), ('Hungarian', 'Hungarian'), ('Pareto', 'Pareto')], max_length=200, null=True),
        ),
    ]
