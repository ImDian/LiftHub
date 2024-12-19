from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Post(models.Model):
    class Meta:
        permissions = [
            ("approve_posts", "Can approve posts"),
            ("delete_posts", "Can delete user posts")
        ]

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    content = models.TextField(
        validators=(
            MaxLengthValidator(300),
        )
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_approved = models.BooleanField(
        default=False,
    )

    has_been_edited = models.BooleanField(
        default=False,
    )


    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        null=True,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
