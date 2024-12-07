from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from LiftHub.meals.forms import MealCreateForm, MealEditForm, MealDeleteForm
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


class MealsDetailsPage(DetailView):
    model = Meal
    template_name = 'meals/meals-details.html'


class MealsEditPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Meal
    template_name = 'meals/edit-meal.html'
    form_class = MealEditForm

    def test_func(self):
        meal = get_object_or_404(Meal, pk=self.kwargs['pk'])
        return self.request.user == meal.creator

    def get_success_url(self):
        return reverse_lazy(
            'meal-details',
            kwargs={
                'pk': self.kwargs['pk'],
            })


class MealsDeletePage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Meal
    template_name = 'meals/delete-meal.html'
    form_class = MealDeleteForm
    success_url = reverse_lazy('meals-home')

    def test_func(self):
        meal = get_object_or_404(Meal, pk=self.kwargs['pk'])
        return self.request.user == meal.creator

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        meal = Meal.objects.get(pk=pk)
        return meal.__dict__


