from django.urls import path
from LiftHub.calculator.views import CalculatorHomePage


urlpatterns = [
    path('', CalculatorHomePage.as_view(), name='calculator-home'),
]
