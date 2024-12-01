from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from LiftHub.forms import CustomUserForm


# Create your views here.


class RegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
