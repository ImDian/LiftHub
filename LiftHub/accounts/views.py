from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from LiftHub.accounts.forms import ProfileEditForm
from LiftHub.accounts.models import Profile
from LiftHub.accounts.models.history import MealHistory
from LiftHub.forms import CustomUserForm
from LiftHub.posts.models import Post


class RegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        reverse_lazy(
            'edit-profile',
            kwargs={
                'slug': self.object.profile.slug,
            })


# TODO fix


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profiles-home.html'
    related_name = 'profile'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profiles/profile-edit.html'
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse_lazy(
            'profile',
            kwargs={
                'slug': self.kwargs['slug'],
            })


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('login')

    def test_func(self):
        profile = get_object_or_404(Profile, user=self.kwargs['user']) # TODO FIX THIS
        return self.request.user == profile.user


class MealHistoryView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = MealHistory
    template_name = 'history/meal-history.html'
    context_object_name = 'meal_history'

    def get_user_from_slug(self):  # helper method
        slug = self.kwargs.get('slug')
        return get_object_or_404(User, username=slug)

    def test_func(self):
        user = self.get_user_from_slug()
        return self.request.user == user

    def get_queryset(self):
        user = self.get_user_from_slug()
        return MealHistory.objects.filter(user=user)


class PostHistoryView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Post
    template_name = 'history/post-history.html'
    context_object_name = 'post_history'

    def get_user_from_slug(self):  # helper method
        slug = self.kwargs.get('slug')
        return get_object_or_404(User, username=slug)

    def test_func(self):
        user = self.get_user_from_slug()
        return self.request.user == user

    def get_queryset(self):
        user = self.get_user_from_slug()
        return Post.objects.filter(user=user)


