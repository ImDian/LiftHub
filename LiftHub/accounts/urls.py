from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from LiftHub.accounts.views import RegisterView, ProfileView, HistoryView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profiles/', include([
        path('', ProfileView.as_view(), name='profile'),
        path('history/', HistoryView.as_view(), name='profile'),
    ]))
]

