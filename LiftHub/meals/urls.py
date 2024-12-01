from django.urls import path

from LiftHub.meals.views import CreateMealView, MealsHomePage

urlpatterns = [
    path('', MealsHomePage.as_view(), name='meals-home'),
    path('create/', CreateMealView.as_view(), name='create-meal'),
]
