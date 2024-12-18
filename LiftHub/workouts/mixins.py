from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from LiftHub.workouts.models import Workout


class WorkoutPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        workout = get_object_or_404(Workout, pk=self.kwargs['pk'])

        if workout.is_base:
            if not request.user.has_perm('workouts.edit_base_workouts'):
                raise PermissionDenied("You do not have permission to edit/delete this workout.")

        else:  # user workout
            if request.user != workout.creator:
                raise PermissionDenied("You can only edit/delete workouts you created.")

        return super().dispatch(request, *args, **kwargs)