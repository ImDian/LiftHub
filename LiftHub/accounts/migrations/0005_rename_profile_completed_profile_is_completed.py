# Generated by Django 4.2.17 on 2024-12-14 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_age_alter_profile_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_completed',
            new_name='is_completed',
        ),
    ]
