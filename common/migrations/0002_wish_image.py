# Generated by Django 5.1.4 on 2025-01-11 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
