from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from LiftHub.meals.forms import MealCreateForm
from LiftHub.meals.models import Meal


class CreateMealView(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealCreateForm
    template_name = 'meals/create-meal.html'
    success_url = reverse_lazy('meals-home')

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.creator = self.request.user

        return super().form_valid(form)


class MealsHomePage(ListView):
    context_object_name = 'meals'
    model = Meal
    template_name = "meals/meals-home.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_meals = Meal.objects.filter(creator=self.request.user)
        else:
            user_meals = Meal.objects.none()
        return user_meals

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_meals'] = Meal.objects.filter(is_base=True)
        return context