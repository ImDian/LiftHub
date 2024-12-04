from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from LiftHub.forms import CustomUserForm


# Create your views here.


class RegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class ProfileView(TemplateView):
    template_name = 'profiles/profiles-home.html'


class HistoryView(TemplateView):
    template_name = 'history/history-home.html'

