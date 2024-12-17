from django.contrib import admin

from LiftHub.workouts.models import Workout


class WorkoutsAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj and not request.user.has_perm('workouts.edit_base_workouts'):
            return False
        return super().has_change_permission(request, obj)


admin.site.register(Workout, WorkoutsAdmin)
