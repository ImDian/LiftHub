from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DetailView, UpdateView, DeleteView
from LiftHub.workouts.forms import WorkoutCreateForm, WorkoutEditForm, WorkoutDeleteForm
from LiftHub.workouts.models import Workout


class CreateWorkoutView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutCreateForm
    template_name = 'workouts/create-workout.html'
    success_url = reverse_lazy('workouts-home')

    def form_valid(self, form):
        workout = form.save(commit=False)
        workout.creator = self.request.user

        return super().form_valid(form)


class WorkoutsHomePage(ListView):
    model = Workout
    context_object_name = 'workouts'
    template_name = "workouts/workouts-home.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_workouts = Workout.objects.filter(creator=self.request.user)
        else:
            user_workouts = Workout.objects.none()
        return user_workouts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_workouts'] = Workout.objects.filter(is_base=True)
        return context


class WorkoutsDetailsPage(UserPassesTestMixin, DetailView):
    model = Workout
    template_name = 'workouts/workouts-details.html'

    def test_func(self):  # can only view details on base workouts and own workouts
        workout = get_object_or_404(Workout, pk=self.kwargs['pk'])
        return self.request.user == workout.creator or workout.is_base


class WorkoutsEditPage(UserPassesTestMixin, UpdateView):
    model = Workout
    template_name = 'workouts/edit-workout.html'
    form_class = WorkoutEditForm

    def test_func(self):
        workout = get_object_or_404(Workout, pk=self.kwargs['pk'])
        return self.request.user == workout.creator

    def get_success_url(self):
        return reverse_lazy(
            'workout-details',
            kwargs={
                'pk': self.kwargs['pk'],
            })


class WorkoutsDeletePage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Workout
    template_name = 'workouts/delete-workout.html'
    form_class = WorkoutDeleteForm
    success_url = reverse_lazy('workouts-home')

    def test_func(self):
        workout = get_object_or_404(Workout, pk=self.kwargs['pk'])
        return self.request.user == workout.creator

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        workout = Workout.objects.get(pk=pk)
        return workout.__dict__
