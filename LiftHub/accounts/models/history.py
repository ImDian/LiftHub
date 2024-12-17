from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from LiftHub.meals.models import Meal
from LiftHub.workouts.models import Workout


UserModel = get_user_model()


class MealHistory(models.Model):
    user = models.ForeignKey(
        to=UserModel,
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
