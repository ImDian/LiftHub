from datetime import date

from django.contrib.auth import get_user_model
from django.db import models

from LiftHub.accounts.choices import GenderChoices

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    height = models.FloatField(
        blank=True,
        null=True,
    )

    weight = models.FloatField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    bmr = models.FloatField(
        blank=True,
        null=True,
    )

    picture = models.ImageField(
        upload_to='profile_pictures/',
        default='default.jpg'
    )

    def get_basic_metabolic_rate(self):
        if self.gender == 'Male':
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        else: # if Female
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)

        return bmr

    def save(self, *args, **kwargs):
        self.bmr = self.get_basic_metabolic_rate()
        super().save(*args, **kwargs)