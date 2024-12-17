from django.contrib import admin
from LiftHub.meals.models import Meal


class MealsAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj and not request.user.has_perm('meals.edit_base_meals'):
            return False
        return super().has_change_permission(request, obj)

admin.site.register(Meal, MealsAdmin)
