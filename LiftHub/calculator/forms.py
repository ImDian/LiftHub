from itertools import chain
from django import forms
from django.db.models import Q

from LiftHub.meals.models import Meal
from LiftHub.workouts.models import Workout

class CalculatorForm(forms.Form):
    meals = forms.ModelMultipleChoiceField(
        queryset=Meal.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Select Meals',
    )

    workouts = forms.ModelMultipleChoiceField(
        queryset=Workout.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Select Workouts',
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.set_meals_and_workouts()

    def set_meals_and_workouts(self):
        combined_meals = Meal.objects.filter(Q(is_base=True) | Q(creator=self.user))

        combined_workouts = Workout.objects.filter(Q(is_base=True) | Q(creator=self.user))

        # Set the queryset for meals and workouts fields
        self.fields['meals'].queryset = combined_meals
        self.fields['workouts'].queryset = combined_workouts

        print("Combined Meals:", combined_meals)
        print("Combined Workouts:", combined_workouts)
        print(self.user)