from django.views.generic import TemplateView


class CalculatorHomePage(TemplateView):
    template_name = 'calculator/calculator-home.html'
