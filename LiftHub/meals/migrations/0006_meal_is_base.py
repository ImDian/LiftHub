# Generated by Django 5.1.3 on 2024-12-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_alter_meal_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='is_base',
            field=models.BooleanField(default=False),
        ),
    ]
