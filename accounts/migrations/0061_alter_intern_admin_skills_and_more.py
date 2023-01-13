# Generated by Django 4.1.2 on 2023-01-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0060_alter_admin_allocation_algorithm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern',
            name='admin_skills',
            field=models.ManyToManyField(blank=True, to='accounts.adminskills'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='analytic_skills',
            field=models.ManyToManyField(blank=True, to='accounts.analyticskills'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='business_skills',
            field=models.ManyToManyField(blank=True, to='accounts.businessskills'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='computing_skills',
            field=models.ManyToManyField(blank=True, to='accounts.computingskills'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='leadership_skills',
            field=models.ManyToManyField(blank=True, to='accounts.leadershipskills'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='management_skills',
            field=models.ManyToManyField(blank=True, to='accounts.managementskills'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='marketing_skills',
            field=models.ManyToManyField(blank=True, to='accounts.marketingskills'),
        ),
    ]
