from django.urls import path

from LiftHub.workouts.views import CreateWorkoutView, WorkoutsHomePage

urlpatterns = [
    path('', WorkoutsHomePage.as_view(), name='workouts-home'),
    path('create/', CreateWorkoutView.as_view(), name='create-workout'),
]
