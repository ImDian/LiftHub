# Generated by Django 4.2.17 on 2024-12-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
