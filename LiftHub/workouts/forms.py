from django import forms

from LiftHub.workouts.models import Workout


class WorkoutBaseForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ['creator', 'is_base']


class WorkoutCreateForm(WorkoutBaseForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if request and request.user.has_perm('workouts.edit_base_workouts'):
            self.fields['is_base'] = self._meta.model._meta.get_field('is_base').formfield()

    def save(self, commit=True):
        workout = super().save(commit=False)
        workout.is_base = self.cleaned_data['is_base']

        if workout.is_base:
            workout.creator = None

        if commit:
            workout.save()

        return workout


class WorkoutEditForm(WorkoutBaseForm):
    pass


class WorkoutDeleteForm(WorkoutBaseForm):
    pass
