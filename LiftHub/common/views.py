from django.views.generic import DetailView, CreateView, TemplateView


class HomePage(TemplateView):
    template_name = "home.html"
