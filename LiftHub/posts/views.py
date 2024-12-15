from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormMixin
from LiftHub.posts.forms import PostCreateForm, PostEditForm, CommentCreateForm
from LiftHub.posts.models import Post, Comment


class ForumHomeView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'all_posts'
    template_name = 'forum/forum-home.html'
    queryset = Post.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['approved_posts'] = Post.objects.filter(is_approved=True).order_by('-created_at')
        context['comments'] = Comment.objects.all()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'forum/create-post.html'
    success_url = reverse_lazy('forum-home')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user

        return super().form_valid(form)


class PostDetailView(FormMixin, LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'forum/post-details.html'
    context_object_name = 'post'
    form_class = CommentCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        context['form'] = self.get_form()
        context['is_editable'] = self.request.user == self.get_object().user
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.get_object()
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.pk})


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'forum/edit-post.html'

    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return self.request.user == post.user

    def form_valid(self, form):
        response = super().form_valid(form)
        post = self.object
        post.has_been_edited = True
        post.save()

        return response

    def get_success_url(self):
        return reverse_lazy(
            'post-details',
            kwargs={
                'pk': self.kwargs['pk'],
            }
        )


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'forum/delete-post.html'
    success_url = reverse_lazy('forum-home')

    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return self.request.user == post.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'forum/create-comment.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.creator = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'post-details',
            kwargs={
                'username': self.kwargs['username'],
                'pk': self.kwargs['pk'],
            }
        )
