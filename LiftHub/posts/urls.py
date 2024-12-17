from django.urls import path, include

from LiftHub.posts import views

urlpatterns = [
    path('', views.ForumHomeView.as_view(), name='forum-home'),
    path('approve/', views.PostApproveView.as_view(), name='post-approve'),
    path('post/', include([
        path('create/', views.PostCreateView.as_view(), name='post-create'),
        path('<pk>/', views.PostDetailView.as_view(), name='post-details'),
        path('<pk>/edit/', views.PostEditView.as_view(), name='post-edit'),
        path('<pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    ]))
]
