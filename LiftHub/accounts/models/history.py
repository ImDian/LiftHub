from django.contrib.auth.models import User
from django.db import models

from LiftHub.meals.models import Meal
from LiftHub.workouts.models import Workout


class History(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    total_calories = models.FloatField()

    total_protein = models.FloatField()

    total_carbs = models.FloatField()

    total_fat = models.FloatField()

    result = models.CharField()

    day = models.DateField(
        auto_now_add=True
    )