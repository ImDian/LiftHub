from django.core.validators import MinValueValidator
from django.db import models

from django.contrib.auth.models import User


class Workout(models.Model):
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

    calories_burned = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.0),
        ]
    )

    creator = models.ForeignKey(
        null=True,
        blank=True,
        to=User,
        on_delete=models.CASCADE,
    )

    def is_base(self):
        return self.creator is None


class WorkoutHistory(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="workout_user",
    )

    workout = models.ForeignKey(
        to=Workout,
        on_delete=models.CASCADE,
        related_name="workout_type",
    )

    date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False,
    )
