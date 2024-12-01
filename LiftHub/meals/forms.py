from django import forms

from LiftHub.meals.models import Meal


class MealBaseForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ['creator']


class MealCreateForm(MealBaseForm):
    pass


class MealEditForm(MealBaseForm):
    pass

