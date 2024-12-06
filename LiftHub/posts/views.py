from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from LiftHub.posts.forms import PostCreateForm
from LiftHub.posts.models import Post


class ForumHomeView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'forum/forum-home.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'forum/create-post.html'
    success_url = '/forum/'


class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post-details.html'



class PostEditView(UpdateView):
    model = Post
    template_name = 'forum/edit-post.html'
    fields = '__all__'