# Generated by Django 5.1.4 on 2025-02-27 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_occupation_profile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
