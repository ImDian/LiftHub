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

    slug = models.SlugField(
        null=False,
        blank=True,
        default='',
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

    bmr = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    picture = models.ImageField(
        upload_to='profile_pictures/',
        default='default.jpg'
    )

    def get_basic_metabolic_rate(self):
        if self.age and self.weight and self.height:
            if self.gender == 'Male':
                bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
            else:  # if Female
                bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)

            self.bmr = int(bmr)

    def save(self, *args, **kwargs):
        self.slug = self.user.username
        self.get_basic_metabolic_rate()
        super().save(*args, **kwargs)
