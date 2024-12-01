from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from LiftHub.workouts.forms import WorkoutCreateForm
from LiftHub.workouts.models import Workout


class CreateWorkoutView(CreateView):
    model = Workout
    form_class = WorkoutCreateForm
    template_name = 'workouts/create-workout.html'
    success_url = reverse_lazy('workouts-home')

    def form_valid(self, form):
        workout = form.save(commit=False)
        workout.creator = self.request.user

        return super().form_valid(form)


class WorkoutsHomePage(TemplateView):
    template_name = "workouts/workouts-home.html"
