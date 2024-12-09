from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

UserModel = get_user_model()


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
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='workouts'
    )

    is_base = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name

