# Generated by Django 4.2.17 on 2024-12-15 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_has_been_edited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='approved',
            new_name='is_approved',
        ),
    ]
