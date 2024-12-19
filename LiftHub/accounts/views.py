from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from LiftHub.accounts.forms import ProfileEditForm
from LiftHub.accounts.models import Profile
from LiftHub.accounts.models.history import MealHistory
from LiftHub.forms import CustomUserForm
from LiftHub.posts.models import Post, Comment

UserModel = get_user_model()


class RegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home-page')


    def form_valid(self, form):
        response = super().form_valid(form)
        backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, self.object, backend=backend)
        return response


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profiles-home.html'
    related_name = 'profile'


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'profiles/profile-edit.html'
    form_class = ProfileEditForm

    def get_user_from_slug(self):  # helper method
        slug = self.kwargs.get('slug')
        return get_object_or_404(UserModel, username=slug)

    def test_func(self):
        user = self.get_user_from_slug()
        return self.request.user == user

    def get_success_url(self):
        return reverse_lazy(
            'profile',
            kwargs={
                'slug': self.kwargs['slug'],
            })

    def form_valid(self, form):
        response = super().form_valid(form)
        profile = self.object
        profile.is_completed = True
        profile.save()

        return response


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home-page')
    context_object_name = 'profile'

    def get_user_from_slug(self):  # helper method
        slug = self.kwargs.get('slug')
        return get_object_or_404(UserModel, username=slug)

    def test_func(self):
        user = self.get_user_from_slug()
        return self.request.user == user

    def form_valid(self, form):
        user = self.object.user
        user.delete()
        return super().form_valid(form)


class MealHistoryView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = MealHistory
    template_name = 'history/meal-history.html'
    context_object_name = 'meal_history'

    def get_user_from_slug(self):  # helper method
        slug = self.kwargs.get('slug')
        return get_object_or_404(UserModel, username=slug)

    def test_func(self):
        user = self.get_user_from_slug()
        return self.request.user == user

    def get_queryset(self):
        user = self.get_user_from_slug()
        return MealHistory.objects.filter(user=user).order_by('-day')


class PostHistoryView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'history/post-history.html'
    context_object_name = 'post_history'

    def get_user_from_slug(self):  # helper method
        slug = self.kwargs.get('slug')
        return get_object_or_404(UserModel, username=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['inspected_user'] = self.get_user_from_slug()
        return context

    def get_queryset(self):
        user = self.get_user_from_slug()
        return Post.objects.filter(user=user)
