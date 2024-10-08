# Generated by Django 4.1.2 on 2022-11-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_adminskills_analyticskills_businessskills_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern',
            name='marketing1_skills',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='job',
            name='marketing1_skills',
            field=models.IntegerField(default=5),
        ),
        migrations.RemoveField(
            model_name='intern',
            name='marketing_skills',
        ),
        migrations.RemoveField(
            model_name='job',
            name='marketing_skills',
        ),
        migrations.AddField(
            model_name='intern',
            name='marketing_skills',
            field=models.ManyToManyField(to='accounts.marketingskills'),
        ),
        migrations.AddField(
            model_name='job',
            name='marketing_skills',
            field=models.ManyToManyField(to='accounts.marketingskills'),
        ),
    ]
