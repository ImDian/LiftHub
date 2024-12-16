from django import forms

from LiftHub.meals.models import Meal


class MealBaseForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ['creator', 'is_base',]


class MealCreateForm(MealBaseForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if request and request.user.has_perm('meals.edit_base_meals'):
            self.fields['is_base'] = self._meta.model._meta.get_field('is_base').formfield()

    def save(self, commit=True):
        meal = super().save(commit=False)
        meal.is_base = self.cleaned_data['is_base']

        if meal.is_base:
            meal.creator = None

        if commit:
            meal.save()

        return meal


class MealEditForm(MealBaseForm):
    pass


class MealDeleteForm(MealBaseForm):
    pass
