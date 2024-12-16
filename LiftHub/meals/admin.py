from django.contrib import admin
from LiftHub.meals.models import Meal


class MealsAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj and obj.is_base and not request.user.has_perm('app.edit_base_meals'):
            return False
        return super().has_change_permission(request, obj)

admin.site.register(Meal, MealsAdmin)
