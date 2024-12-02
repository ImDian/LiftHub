from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from LiftHub.workouts.forms import WorkoutCreateForm
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