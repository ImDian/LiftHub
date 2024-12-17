from django.contrib import admin
from LiftHub.posts.models import Post


class PostsAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        if obj and not request.user.has_perm('posts.delete_posts'):
            return False
        return super().has_delete_permission(request, obj)

    def can_approve_posts(self, request, obj=None):
        if obj and not request.user.has_perm('posts.approve_posts'):
            return False
        return request.user.has_perm('posts.approve_posts')

admin.site.register(Post, PostsAdmin)

