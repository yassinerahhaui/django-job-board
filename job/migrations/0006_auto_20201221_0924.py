# Generated by Django 3.1.4 on 2020-12-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=100, null=True),
        ),
    ]
