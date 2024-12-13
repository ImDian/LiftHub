from math import floor

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from LiftHub.accounts.choices import SexChoices

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
        validators=[
            MinValueValidator(0),
        ]
    )

    weight = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
        ]
    )

    sex = models.CharField(
        max_length=1,
        choices=SexChoices.choices,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,validators=[
            MinValueValidator(1),
        ]
    )

    bmr = models.PositiveIntegerField(
        blank=True,
        null=False,
        default=0,
        validators=[
            MinValueValidator(0),
        ]
    )

    body_fat = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
        ]
    )

    picture = models.ImageField(
        upload_to='profile_picture/',
        default='profile_picture/default_pfp.jpg',
        blank=True,
        null=False,
    )

    def get_basic_metabolic_rate(self):
        if self.body_fat:  # use more accurate formula
            lean_body_mass = self.weight * (1 - (self.body_fat / 100))
            self.bmr = floor(370 + (21.6 * lean_body_mass))

        elif self.age and self.weight and self.height:  # use a less accurate formula
            if self.sex == 'Male':
                bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
            else:  # if Female
                bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)

            self.bmr = int(bmr)

    def save(self, *args, **kwargs):
        self.slug = self.user.username
        self.get_basic_metabolic_rate()
        if not self.picture:
            self.picture = 'profile_picture/default_pfp.jpg'
        super().save(*args, **kwargs)
