from django.urls import reverse_lazy
from django.views.generic import FormView

from LiftHub.accounts.models.history import History
from LiftHub.calculator.forms import CalculatorForm


class CalculatorHomePage(FormView):
    template_name = 'calculator/calculator-home.html'
    form_class = CalculatorForm
    success_url = reverse_lazy('calculator-home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        action = self.request.POST.get('action', 'calculate')

        if action == 'calculate':
            selected_meals = form.cleaned_data['meals']

            total_calories = sum(meal.calories for meal in selected_meals)
            total_protein = sum(meal.protein for meal in selected_meals)
            total_carbs = sum(meal.carbs for meal in selected_meals)
            total_fat = sum(meal.fat for meal in selected_meals)

            selected_workouts = form.cleaned_data['workouts']

            total_burned_calories = sum(workout.calories_burned for workout in selected_workouts)
            remaining_calories = total_calories - total_burned_calories

            if remaining_calories > 0:
                result = f'{remaining_calories} calories surplus.'
            elif remaining_calories < 0:
                result = f'{remaining_calories} calories deficit.'
            else:
                result = 'caloric maintenance.'

            context = self.get_context_data(
                form=form,
                total_calories=total_calories,
                total_protein=total_protein,
                total_carbs=total_carbs,
                total_fat=total_fat,
                selected_meals=selected_meals,
                selected_workouts=selected_workouts,
                remaining_calories=remaining_calories,
                total_burned_calories=total_burned_calories,
                result=result,
                show_save_button=True
            )
            return self.render_to_response(context)

        elif action == 'save':

            total_calories = float(self.request.POST.get('total_calories', 0))
            total_protein = float(self.request.POST.get('total_protein', 0))
            total_carbs = float(self.request.POST.get('total_carbs', 0))
            total_fat = float(self.request.POST.get('total_fat', 0))
            result = str(self.request.POST.get('result', ''))

            if self.request.user.is_authenticated:
                History.objects.create(
                    user=self.request.user,
                    total_calories=total_calories,
                    total_protein=total_protein,
                    total_carbs=total_carbs,
                    total_fat=total_fat,
                    result=result,
                )

            context = self.get_context_data(
                form=form,
                message="Meal history saved successfully!",
            )

            return self.render_to_response(context)

        return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

