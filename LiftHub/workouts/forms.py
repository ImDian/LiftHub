from django import forms

from LiftHub.workouts.models import Workout


class WorkoutBaseForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ['creator', 'is_base']


class WorkoutCreateForm(WorkoutBaseForm):
    pass


class WorkoutEditForm(WorkoutBaseForm):
    pass
