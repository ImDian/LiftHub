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

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name

        return self.first_name or self.last_name or "Anonymous"