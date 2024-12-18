from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormMixin
from LiftHub.posts.forms import PostCreateForm, PostEditForm, CommentCreateForm
from LiftHub.posts.mixins import PostPermissionMixin
from LiftHub.posts.models import Post, Comment


class ForumHomeView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'approved_posts'
    template_name = 'forum/forum-home.html'
    queryset = Post.objects.filter(is_approved=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['awaiting_count'] = Post.objects.filter(is_approved=False).count()
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
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-created_at')
        context['form'] = self.get_form()
        context['has_permission'] = (
                self.request.user == self.get_object().user or
                self.request.user.has_perm('posts.delete_posts')
        )
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


class PostEditView(LoginRequiredMixin, PostPermissionMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'forum/edit-post.html'

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


class PostDeleteView(LoginRequiredMixin, PostPermissionMixin, DeleteView):
    model = Post
    template_name = 'forum/delete-post.html'
    success_url = reverse_lazy('forum-home')


class PostApproveListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'forum/approve-posts.html'
    queryset = Post.objects.filter(is_approved=False)
    context_object_name = 'unapproved_posts'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('posts.approve_posts'):
            raise PermissionDenied("You do not have permission to view this page.")
        return super().dispatch(request, *args, **kwargs)


@permission_required('posts.approve_posts', raise_exception=True)
def approve_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.is_approved = True
    post.save()

    return redirect(request.META.get('HTTP_REFERER'))
