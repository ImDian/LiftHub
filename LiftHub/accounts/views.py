from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, DetailView
from LiftHub.accounts.models import Profile
from LiftHub.accounts.models.history import History
from LiftHub.forms import CustomUserForm


class RegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profiles-home.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profiles/profiles-home.html'
    success_url = ''


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profiles/profiles-home.html'


class HistoryView(TemplateView):
    model = History
    template_name = 'history/history-home.html'
