from django.urls import path, include

from LiftHub.workouts import views
urlpatterns = [
    path('', views.WorkoutsHomePage.as_view(), name='workouts-home'),
    path('create/', views.CreateWorkoutView.as_view(), name='create-workout'),
    path('workout/<int:pk>/', include([
        path('', views.WorkoutsDetailsPage.as_view(), name='workout-details'),
        path('edit/', views.WorkoutsEditPage.as_view(), name='workout-edit'),
        path('delete/', views.WorkoutsDeletePage.as_view(), name='delete-workout'),
    ]))
]
