"""
URL configuration for LiftHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from LiftHub import settings
from LiftHub.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('admin/', admin.site.urls),
    path('accounts/', include('LiftHub.accounts.urls')),
    path('meals/', include('LiftHub.meals.urls')),
    path('workouts/', include('LiftHub.workouts.urls')),
    path('calculator/', include('LiftHub.calculator.urls')),
    path('forum/', include('LiftHub.posts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
