from django.urls import path, include

from LiftHub.meals import views

urlpatterns = [
    path('', views.MealsHomePage.as_view(), name='meals-home'),
    path('create/', views.CreateMealView.as_view(), name='create-meal'),
    path('meal/<int:pk>/', include([
        path('', views.MealsDetailsPage.as_view(), name='meal-details'),
        path('edit/', views.MealsEditPage.as_view(), name='edit-meal'),
        path('delete/', views.MealsDeletePage.as_view(), name='delete-meal'),
    ]))
]
