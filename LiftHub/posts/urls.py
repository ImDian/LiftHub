from django.urls import path, include

from LiftHub.posts import views

urlpatterns = [
    path('', views.ForumHomeView.as_view(), name='forum-home'),
    path('post/', include([
        path('create/', views.PostCreateView.as_view(), name='create-post'),
        path('<pk>/', views.PostDetailView.as_view(), name='post-details'),
        path('<pk>/edit/', views.PostEditView.as_view(), name='edit-post'),
    ]))
]
