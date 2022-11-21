# Generated by Django 4.1.2 on 2022-11-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_admin_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='phase',
            field=models.CharField(choices=[('Job', 'Job creation'), ('Intern', 'Intern collection'), ('Allocate', 'Allocation')], max_length=200, null=True),
        ),
    ]
