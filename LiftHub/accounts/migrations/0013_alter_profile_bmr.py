# Generated by Django 4.2.17 on 2024-12-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rename_history_mealhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bmr',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]