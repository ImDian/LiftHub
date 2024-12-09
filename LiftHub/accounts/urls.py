from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from LiftHub.accounts.views import RegisterView, ProfileView, MealHistoryView, ProfileEditView, PostHistoryView, \
    ProfileDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profiles/<slug:slug>/', include([
        path('', ProfileView.as_view(), name='profile'),
        path('edit/', ProfileEditView.as_view(), name='edit-profile'),
        path('history/', MealHistoryView.as_view(), name='meal-history'),
        path('posts/', PostHistoryView.as_view(), name='post-history'),
        path('delete/', ProfileDeleteView.as_view(), name='delete-profile'),
    ]))
]

