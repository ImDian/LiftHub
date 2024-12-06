from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

UserModel = get_user_model()

class Meal(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=300,
        null=True,
        blank=True,
    )

    calories = models.FloatField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0.0),
        ]
    )

    protein = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.0),
        ]
    )

    fat = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.0),
        ]
    )

    carbs = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.0),
        ]
    )

    creator = models.ForeignKey(
        null=True,
        blank=True,
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='meals'
    )

    is_base = models.BooleanField(
        default=False,
    )

    def calculate_calories(self):
        cals_from_carbs = self.carbs * 4.0
        cals_from_protein = self.protein * 4.0
        cals_from_fat = self.fat * 9.0
        total_calories = cals_from_carbs + cals_from_protein + cals_from_fat
        return total_calories

    def save(self, *args, **kwargs):
        if self.calories is None:
            self.calories = self.calculate_calories()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
