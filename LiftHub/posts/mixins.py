from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from LiftHub.posts.models import Post


class PostPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])

        if request.user != post.user:
            if not request.user.has_perm('posts.delete_posts'):
                raise PermissionDenied("You do not have permission to edit/delete this post.")

        return super().dispatch(request, *args, **kwargs)