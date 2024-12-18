from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from LiftHub.meals.models import Meal


class MealPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        meal = get_object_or_404(Meal, pk=self.kwargs['pk'])

        if meal.is_base:
            if not request.user.has_perm('meals.edit_base_meals'):
                raise PermissionDenied("You do not have permission to edit/delete this meal.")

        else: # user meal
            if request.user != meal.creator:
                raise PermissionDenied("You can only edit/delete meals you created.")

        return super().dispatch(request, *args, **kwargs)
