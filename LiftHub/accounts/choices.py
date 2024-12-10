from django.db import models


class SexChoices(models.TextChoices):
    MALE = "M", 'Male'
    FEMALE = "F", 'Female'