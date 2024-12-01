from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView

from LiftHub.meals.forms import MealCreateForm
from LiftHub.meals.models import Meal


class CreateMealView(CreateView):
    model = Meal
    form_class = MealCreateForm
    template_name = 'meals/create-meal.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.creator = self.request.user

        return super().form_valid(form)


class MealsHomePage(TemplateView):
    template_name = "meals/meals-home.html"
