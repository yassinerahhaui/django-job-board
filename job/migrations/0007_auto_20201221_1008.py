# Generated by Django 3.1.4 on 2020-12-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20201221_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
