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
        if self.user.is_authenticated:
            display_meals = Meal.objects.filter(Q(is_base=True) | Q(creator=self.user))  # base + user meals
            display_workouts = Workout.objects.filter(Q(is_base=True) | Q(creator=self.user))  # base + user workouts

        else:
            display_meals = Meal.objects.filter(is_base=True)
            display_workouts = Workout.objects.filter(is_base=True)

        self.fields['meals'].queryset = display_meals
        self.fields['workouts'].queryset = display_workouts

